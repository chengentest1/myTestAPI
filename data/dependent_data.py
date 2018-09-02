from util.operation_excel import OperationExcel


class Dependent:
    def get_depentdent_data(self,id):
        opera = OperationExcel()
        vak=opera.get_rows_data(id)
        dic_data={"url":vak[2],"method":vak[3],"type":vak[4],"header":vak[5],"data":vak[6],"result":vak[7]}
        return dic_data





if __name__=="__main__":
    u=Dependent().get_depentdent_data('one')
    print(u)