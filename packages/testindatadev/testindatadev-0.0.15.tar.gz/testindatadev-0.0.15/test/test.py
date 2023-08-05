from testindatadev.TDA import TDA

T_key = "0fbe149adf07e5f4afa01a7a4e787fde"
ip = "10.32.144.73"

tda = TDA(T_key, debug=True)

tda.Debug()

dataset = tda.SetDataset("ds_7_hxflkjegen8hmucubk", ip)

metaData = {
    "metaKey1":"metaVal1",
    "metaKey2":"metaVal2",
    "metaKey3":"metaVal3",
}

file = tda.AddFile("/Users/hejinlong/Desktop/test_pic/11.jpg", referId="myTestRefId", metaData=metaData)

box = {
    "x": 10,
    "y": 10,
    "width": 100,
    "height": 100,
}

label = "myTestLabelName"

attr = {
    "attrKey1":"attrVal1",
    "attrKey2":"attrVal2",
    "attrKey3":"attrVal3",
}

file.AddBox2D(box, label=label, attrs=attr)

print(tda.Upload())
