from testindatadev.TDA import TDA
import sys
import os
import json

# T_key = "0fbe149adf07e5f4afa01a7a4e787fde"
# ip = "10.32.141.220"
# ds = "ds_ihtxzc_uhocslt4fjhrc"

# T_key = "492535c229015dcd8de80e2ad64c299b"
# ip = "10.10.32.54"
# ds = "ds_ge4msswcrghbofy91tuw"

T_key = "bb76998774f7c1347fe347369a4ed470"
ip = "dataset.testin.cn"
ds = "ds_lvsq4xd2obicciiwf6nk"


tda = TDA(T_key)
tda.Debug()
dataset = tda.SetDataset(ds, ip)

path = "/Users/hejinlong/Desktop/数据集测试数据/图像/多边形/pic"

i = 0
for root, dirs, files in os.walk(path):
    for filename in files:
        if filename.endswith(".jpg"):
            filepath = os.path.join(root, filename)
            jsonPath = os.path.join("/Users/hejinlong/Desktop/数据集测试数据/图像/多边形/json", filename + ".json")

            file = tda.AddFile(filepath)

            with open(jsonPath) as jf:
                jsonData = json.load(jf)

                polygonArr = []
                for mark in jsonData["marks"]:
                    polygonArr.append(mark)
                polygonArr.reverse()

                index = 0
                for mark in polygonArr:
                    if mark["type"] == "polygon":
                        attr = {
                            "type": mark["property"][0][0]["ptitle"],
                            "pname": mark["property"][0][0]["pname"],
                            "pselect": mark["pselect"],
                        }
                        index += 1
                        file.AddPolygon(mark["point"], label=mark["property"][0][0]["ptitle"], attrs=attr, index=index)


print(tda.Upload())
