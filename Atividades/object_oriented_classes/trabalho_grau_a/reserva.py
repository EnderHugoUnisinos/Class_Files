from utils import Utils
class Reserva:
    def __init__ (self, dia_inicio = None, dia_fim = None, cliente = None, quarto = None, status = 'A'):
        self.dia_inicio = dia_inicio
        self.dia_fim = dia_fim
        self.cliente = cliente
        self.quarto = quarto
        self.status = status
    
    def __str__(self):
        dias = self.contar_dias()
        return f"Cliente: {self.get_cliente()}, Dia de inicio: {self.get_datas()[0]}, Dia final: {self.get_datas()[1]}, Total de dias: {dias}, Status: {self.get_status()}"
    
    def __repr__(self):
        return f'Reserva({self.get_datas()[0]},{self.get_datas()[1]},{self.get_cliente()},{self.get_quarto()},{self.get_status()})'
    
    def get_cliente(self):
        return self.cliente
    def get_quarto(self):
        return self.quarto
    def get_status(self):
        return self.status
    def get_datas(self):
        data = [self.dia_inicio,self.dia_fim]
        return data
    
    def set_cliente(self, cliente):
        self.cliente = cliente
    def set_quarto(self, quarto):
        self.quarto = quarto
    def set_status(self, status):
        self.status = status
    def set_data(self, data):
        self.dia_inicio = data[0]
        self.dia_fim = data[1]

    def contar_dias(self):
        return Utils().contar_dias(self.get_datas())
    
    def calcular_diaria(self):
        dias = self.contar_dias()
        total = dias * self.get_quarto().get_diaria()
        return total

    def serializar(self):
        serialized_string = "{}/{}/{}/{}/{}".format(self.get_datas()[0], self.get_datas()[1], self.get_cliente(), self.get_quarto().get_numero(), self.get_status())
        return serialized_string

    def deserializar(self, string, quartos):
        split_string = string.strip().split("/")
        split_string[0] #dia inicio
        split_string[1] #dia fim
        split_string[2] #cliente
        split_string[3] #numero do quarto
        split_string[4] #status
        
        self.set_data([split_string[0], split_string[1]])
        self.set_cliente(split_string[2])
        for i in quartos:
            if i.numero == split_string[3]:
                self.set_quarto(i)
                break
        self.set_status(split_string[4])
        return self