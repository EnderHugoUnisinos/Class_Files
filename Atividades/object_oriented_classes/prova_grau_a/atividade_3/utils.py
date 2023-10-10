class Utils:
    def validar_formato_data(self, string):
        try:
            int_list = self.separate_date(string)
            if int_list[0] != 0 and int_list[1] != 0 and int_list[1] <= 12 and int_list[2] != 0:
                validation_result = True
            else:
                validation_result = False
        except:
            validation_result = False
        return validation_result
    
    def separate_date(self, string):
        split_string = string.split("/")
        int_list = [int(split_string[0]),int(split_string[1]),int(split_string[2])]
        return int_list    
    
    def comparar_datas(self, data1, data2):
        result = None
        sep_data1 = self.separate_date(data1)
        sep_data2 = self.separate_date(data2)
        sep_data_total = [(sep_data1[0]-sep_data2[0]),(sep_data1[1]-sep_data2[1]),(sep_data1[2]-sep_data2[2])]
        for i in range(3):
            if sep_data_total[i] < 0 and i != 2:
                sep_data_total[i+1] -= 1
        dif_ano = sep_data_total[2]
        if dif_ano < 0:
            result = -1
        elif dif_ano > 0:
            result = 1
        else:
            result = 0
            
        return result    
        