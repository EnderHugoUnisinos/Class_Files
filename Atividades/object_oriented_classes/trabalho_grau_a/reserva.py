class Reserva:
    def __init__ (self, dia_inicio, dia_fim, cliente, quarto, status = 'A'):
        self.dia_inicio = dia_inicio
        self.dia_fim = dia_fim
        self.cliente = cliente
        self.quarto = quarto
        self.status = status
    
    def get_cliente(self):
        return self.cliente

    def get_quarto(self):
        return self.quarto

    def get_data(self):
        data = [self.dia_inicio,self.dia_fim]
        return data

    def set_status(self, status):
        self.status = status

    def serializar(self):
        pass

    def deserializar(self):
        pass