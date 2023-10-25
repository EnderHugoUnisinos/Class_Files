from datetime import datetime

class Utils:
    @staticmethod
    def validar_formato_data(string):
        date_format = "%d/%m/%Y"
        try:
            datetime.strptime(string, date_format)
            return True
        except ValueError:
            return False
    @staticmethod
    def separate_date(string):
        split_string = string.split("/")
        int_list = [int(split_string[0]),int(split_string[1]),int(split_string[2])]
        return int_list 
    @staticmethod
    def comparar_datas(data1, data2):
        date_format = "%d/%m/%Y"

        data1_obj = datetime.strptime(data1, date_format)
        data2_obj = datetime.strptime(data2, date_format)
        
        if data1_obj > data2_obj:
            return 1
        elif data1_obj < data2_obj:
            return -1
        else:
            return 0
            