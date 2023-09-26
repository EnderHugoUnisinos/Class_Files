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
        consumo_string = ""
        for j in self.quarto.lista_consumo():
            consumo_string = "{}{}:".format(consumo_string, j)
        serialized_string = "{}/{}/{}/{}|{}|{}|{}".format(self.dia_inicio, self.dia_fim, self.cliente, self.quarto.numero, self.quarto.categoria, self.quarto.diaria, consumo_string, self.status)
        return serialized_string

    def deserializar(self):
        pass