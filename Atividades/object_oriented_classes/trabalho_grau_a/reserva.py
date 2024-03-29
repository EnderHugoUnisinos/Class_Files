from utils import Utils
class Reserva:
    def __init__ (self, __diaInicio = None, __diaFim = None, __cliente = None, __quarto = None, __status = 'A'):
        self.diaInicio = __diaInicio
        self.diaFim = __diaFim
        self.cliente = __cliente
        self.quarto = __quarto
        self.status = __status
    
    def __str__(self) -> str:
        dias = self.contarDias()
        return f"Cliente: {self.getCliente()}, Dia de inicio: {self.getDatas()[0]}, Dia final: {self.getDatas()[1]}, Total de dias: {dias}, Status: {self.getStatus()}"
    def __repr__(self):
        return f'Reserva({self.getDatas()[0]},{self.getDatas()[1]},{self.getCliente()},{self.getQuarto()},{self.getStatus()})'
    
    #redundancy to follow the code schematics
    def toString(self):
        dias = self.contarDias()
        return f"Cliente: {self.getCliente()}, Dia de inicio: {self.getDatas()[0]}, Dia final: {self.getDatas()[1]}, Total de dias: {dias}, Status: {self.getStatus()}"

    def getCliente(self):
        return self.cliente
    def getQuarto(self):
        return self.quarto
    def getStatus(self):
        return self.status
    def getDatas(self):
        data = [self.diaInicio,self.diaFim]
        return data
    
    def setCliente(self, cliente):
        self.cliente = cliente
    def setQuarto(self, quarto):
        self.quarto = quarto
    def setStatus(self, status):
        self.status = status
    def setData(self, data):
        self.diaInicio = data[0]
        self.diaFim = data[1]

    def contarDias(self):
        return Utils().countDays(self.getDatas())
    
    def calcularDiaria(self):
        dias = self.contarDias()
        total = dias * self.getQuarto().getDiaria()
        return total

    def serializar(self):
        serializedString = "{}/{}/{}/{}/{}".format(self.getDatas()[0], self.getDatas()[1], self.getCliente(), self.getQuarto().getNumero(), self.getStatus())
        return serializedString

    def deserializar(self, string, quartos):
        splitString = string.strip().split("/")
        splitString[0] #dia inicio
        splitString[1] #dia fim
        splitString[2] #cliente
        splitString[3] #numero do quarto
        splitString[4] #status
        
        self.setData([splitString[0], splitString[1]])
        self.setCliente(splitString[2])
        for i in quartos:
            if i.numero == splitString[3]:
                self.setQuarto(i)
                break
        self.setStatus(splitString[4])
        return self