class Utils:
    def verificar_data_overlap(self, data_reservada, data_teste):
        data_reservada_separated = [data_reservada[0].split("-"),data_reservada[1].split("-")]
        data_teste_separated = [data_teste.split("-")]
        
        data_reservada_separated = {"start": {"day": int(data_reservada_separated[0][0]),"month": int(data_reservada_separated[0][1]),"year" : int(data_reservada_separated[0][2])}, "ending": {"day": int(data_reservada_separated[1][0]),"month": int(data_reservada_separated[1][1]),"year" : int(data_reservada_separated[1][2])}}
        data_teste_separated = {"day": int(data_teste_separated[0][0]),"month": int(data_teste_separated[0][1]),"year" : int(data_teste_separated[0][2])}

        day = data_reservada_separated["start"]["day"]
        month = data_reservada_separated["start"]["month"]
        year = data_reservada_separated["start"]["year"]
        
        overlap_found = False

        while True:
            if day > 31:
                day = 0
                month += 1
            if month > 12:
                month = 0
                year += 1
            if day == data_reservada_separated["ending"]["day"] and month == data_reservada_separated["ending"]["month"] and year == data_reservada_separated["ending"]["year"]:
                break
            if day == data_teste_separated["day"] and month == data_teste_separated["month"] and year == data_teste_separated["year"]:
                overlap_found = True
            day += 1
        return overlap_found

    def validar_formato_data(self, string):
        try:
            split_string = string.split("-")
            int_list = [int(split_string[0]),int(split_string[1]),int(split_string[2])]
            if int_list[0] != 0 and int_list[1] != 0 and int_list[2] != 0:
                validation_result = True
            else:
                validation_result = False
        except:
            validation_result = False
        return validation_result
    
    def validar_formato_numero_quarto(self, string):
        try:
            numero = int(string)
            if numero > 0:
                validation_result = True
            else:
                validation_result = False
        except:
            validation_result = False
        return validation_result