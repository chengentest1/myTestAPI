import xlrd


class OperationExcel:
    def __init__(self,file_name=None,sheet_id=0):
        if file_name:
            self.file_name=file_name
            self.sheet_id=sheet_id
        else:
            self.file_name='../dataconfig/case.xlsx'
            self.sheet_id=sheet_id
        self.data=self.get_data()
    #获取sheet的内容
    def get_data(self):
        data=xlrd.open_workbook(self.file_name)
        tables=data.sheet_by_index(self.sheet_id)
        return tables
    #获取单元格的行数
    def get_lines(self):
        tables=self.data
        return tables.nrows
    #获取某一个单元格的内容
    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)
