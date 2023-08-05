from qiniu import Auth, put_file, etag
import qiniu.config

class Qiniu():
    def __init__(self, req=None):
        self.upload_token = ""
        self.req = req


    #上传单个文件数据
    def PutObject(self, bucketName, objectName, filePath, content_type='application/octet-stream', metadata=None):
        if self.upload_token == "":
            urlInfo = self.req.GetUploadUrl(objectName)
            self.upload_token = urlInfo["url"]
        try:
            ret, info = put_file(self.upload_token, objectName, filePath)
        except:
            raise Exception("failed in putting file")
