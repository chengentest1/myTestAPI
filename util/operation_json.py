import json
class OperationJson:
    def __init__(self,file_path=None):
        if file_path==None:
            self.file_path='../dataconfig/user.json'
        else:
            self.file_path=file_path
        self.data=self.read_data()
    #读取json文件
    def read_data(self):
        with open(self.file_path) as fp:
            data=json.load(fp)
        return data
    #根据关键字获取数据
    def get_data_json(self,key):
        return self.data[key]
    #写json
    def write_data(self,data):
        with open('../dataconfig/passwd.json') as fp:
            fp.write(json.dumps(data))
if __name__=="__main__":
    ui=OperationJson('../dataconfig/passwd.json')
    value=ui.get_data_json('headers')
    print(value)