from utils import Utils

class Data():
    def __init__(self, data):
        if (Utils().validar_formato_data(data)):
            self.data = data
        else:
            data = "01/01/0001"
        
    def __str__(self):
        return f"Data: {self.getData()}, Dia:{self.getDia()}, Mês:{self.getMes()}, Mês por extenso: {self.getMesExtenso()}, Ano: {self.getAno()}, Bissexto?: {self.isBissexto()}"
        
    def __repr__(self):
        return f"Data:({self.getData()})"
    
    def getData(self):
        return self.data
    def setData(self, data):
        if (Utils().validar_formato_data(data)):
            self.data = data
        else:
            data = "01/01/0001"
    
    def compara(self, data):
        result = Utils().comparar_datas(self.getData(), data.getData())
        return result
    
    def getDia(self):
        return Utils().separate_date(self.getData())[0]
    
    def getMes(self):
        return Utils().separate_date(self.getData())[1]
    
    def getMesExtenso(self):
        mes_dict = {1:"Janeiro",2:"Fevereiro",3:"Março",4:"Abril",5:"Maio",6:"Junho",7:"Julho",8:"Agosto",9:"Setembro",10:"Outubro",11:"Novembro",12:"Dezembro"}
        mes_ext = mes_dict[self.getMes()]
        return mes_ext
        
    def getAno(self):
        return Utils().separate_date(self.getData())[2]
    
    def isBissexto(self):
        if (self.getAno() % 4) == 0:
            return True
        else:
            return False