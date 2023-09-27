class Utils:
    def verificar_data_overlap(self, data_reservada, data_teste):
        data_reservada_separated = [data_reservada[0].split("-"),data_reservada[1].split("-")]
        data_teste_separated = [data_teste[0].split("-"),data_teste[1].split("-")]
        
        data_reservada_separated = {"start": {"day": int(data_reservada_separated[0][0]),"month": int(data_reservada_separated[0][1]),"year" : int(data_reservada_separated[0][2])}, "ending": {"day": int(data_reservada_separated[1][0]),"month": int(data_reservada_separated[1][1]),"year" : int(data_reservada_separated[1][2])}}
        data_teste_separated = {"start": {"day": int(data_teste_separated[0][0]),"month": int(data_teste_separated[0][1]),"year" : int(data_teste_separated[0][2])}, "ending": {"day": int(data_teste_separated[1][0]),"month": int(data_teste_separated[1][1]),"year" : int(data_teste_separated[1][2])}}

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

            if day == data_teste_separated["start"]["day"] and month == data_teste_separated["start"]["month"] and year == data_teste_separated["start"]["year"]:
                overlap_found = True
            if day == data_teste_separated["ending"]["day"] and month == data_teste_separated["ending"]["month"] and year == data_teste_separated["ending"]["year"]:
                overlap_found = True

            day += 1
        
        return overlap_found
    