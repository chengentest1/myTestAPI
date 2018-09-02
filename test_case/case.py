import json
import unittest

import ddt

from base.runmethod import RunMethod
from data.get_excel_data import getExcelData
from util.add_header import addHeader
from util.operation_excel import OperationExcel
from util.operation_json import OperationJson
from util.operation_mysql import user

data_test=getExcelData()
@ddt.ddt
class MyTest(unittest.TestCase):
    def setUp(self):
        print('测试用例开始')

    def tearDown(self):
        use=user()
        use.del_user(self.user_name)
        print('测试用例结束')
    @ddt.data(*data_test)
    def test_api(self,data_case):
        self.id=data_case["id"]
        self.casename=data_case["casename"]
        self.url=data_case['url']
        self.method=data_case["method"]
        self.type=data_case['type']
        self.header=data_case['header']
        self.data=data_case['data']
        self.expect=data_case['expect']
        self.reslut=data_case['result']
        self.stuta=data_case['statu']
        self.is_dependent=data_case['is_dependent']
        self.dependent_id=data_case['dependent_id']
        self.dependent_name=data_case['dependent_name']
        ui = OperationJson('../dataconfig/passwd.json')
        if self.header:
            self.header=ui.get_data_json(self.header)
            self.jk=ui.get_data_json(self.data)
            self.user_name=self.jk['name']
            self.data=json.dumps(self.jk)
        else:
            self.header = None
            self.data=ui.get_data_json(self.data)
        run_method = RunMethod()
        # # print(self.method,self.url,self.data,self.header)
        try:
            api=run_method.run_main(method=self.method,url=self.url,data=self.data,headers=self.header)
        except Exception as e:
            pass
        print(api)
        # print(self.method,self.casename,self.url,self.id)
if __name__=="__main__":
    unittest.main()




