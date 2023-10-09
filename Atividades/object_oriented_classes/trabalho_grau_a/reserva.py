from utils import Utils
class Reserva:
    def __init__ (self, diaInicio = None, diaFim = None, cliente = None, quarto = None, status = 'A'):
        self.diaInicio = diaInicio
        self.diaFim = diaFim
        self.cliente = cliente
        self.quarto = quarto
        self.status = status
    
    def __str__(self):
        dias = self.contarDias()
        return f"Cliente: {self.getCliente()}, Dia de inicio: {self.getDatas()[0]}, Dia final: {self.getDatas()[1]}, Total de dias: {dias}, Status: {self.getStatus()}"
    
    def __repr__(self):
        return f'Reserva({self.getDatas()[0]},{self.getDatas()[1]},{self.getCliente()},{self.getQuarto()},{self.getStatus()})'
    
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
        total = dias * self.getquarto().getDiaria()
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