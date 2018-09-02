from util.operation_excel import OperationExcel

def getExcelData():
    opera=OperationExcel()
    rows=opera.get_lines()
    make_data=[]
    for i in range(1,rows):
        id=opera.get_cell_value(i,0)
        casename=opera.get_cell_value(i,1)
        url=opera.get_cell_value(i,2)
        method=opera.get_cell_value(i,3)
        type=opera.get_cell_value(i,4)
        header=opera.get_cell_value(i,5)
        data=opera.get_cell_value(i,6)
        expect=opera.get_cell_value(i,7)
        reslut=opera.get_cell_value(i,8)
        stuta=opera.get_cell_value(i,9)
        is_dependent=opera.get_lines(i,10)
        dependent_id=opera.get_cell_value(i,11)
        dependent_name=opera.get_cell_value(i,12)

        make_data.append({"id":id,"casename":casename,'url':url,"method":method,'type':type,"data":data,"header":header,\
                         "expect":expect,"result":reslut,"statu":stuta,"is_dependent":is_dependent,\
                          "dependent_id":dependent_id,"dependent_name":dependent_name})
    return make_data

