from util.operation_excel import OperationExcel

def getExcelData():
    opera=OperationExcel()
    rows=opera.get_lines()
    make_data=[]
    for i in range(1,rows):
        id=opera.get_cell_value(i,0)
        name=opera.get_cell_value(i,1)
        url=opera.get_cell_value(i,2)
        method=opera.get_cell_value(i,3)
        type=opera.get_cell_value(i,4)
        header=opera.get_cell_value(i,5)
        data=opera.get_cell_value(i,6)
        expect=opera.get_cell_value(i,7)
        reslut=opera.get_cell_value(i,8)
        stuta=opera.get_cell_value(i,9)

        make_data.append({'url':url,"method":method,'type':type,"data":data,"header":header})
    return make_data

h=getExcelData()
print(h)