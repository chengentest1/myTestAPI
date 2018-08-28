import json
import unittest

import ddt

from base.runmethod import RunMethod
from data.get_excel_data import getExcelData
from util.add_header import addHeader
from util.operation_excel import OperationExcel
from util.operation_json import OperationJson

data_test=getExcelData()
@ddt.ddt
class MyTest(unittest.TestCase):
    def setUp(self):
        print('测试用例开始')

    def tearDown(self):
        print('测试用例结束')
    @ddt.data(*data_test)
    def test_api(self,data_case):
        self.id=data_test['id']
        self.name=data_test['name']
        self.url=data_test['url']
        self.method=data_test['method']
        self.type=data_test['type']
        self.header=data_test['header']
        self.data=data_test['data']
        self.expect=data_test['expect']
        self.reslut=data_test['reslut']
        self.stuta=data_test['stuta']
        if self.header =="no":
            self.header=None
        else:
            ui = OperationJson()
            self.header=ui.get_data(self.header)
            self.data=json.dumps(self.data)
        run_method = RunMethod()
        api=run_method.run_main(method=data_test['method'],url=data_test['url'],data=data_test['data'],headers=data_test['headers'])




