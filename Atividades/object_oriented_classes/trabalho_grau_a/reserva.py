class Reserva:
    def __init__ (self, dia_inicio = None, dia_fim = None, cliente = None, quarto = None, status = 'A'):
        self.dia_inicio = dia_inicio
        self.dia_fim = dia_fim
        self.cliente = cliente
        self.quarto = quarto
        self.status = status
    
    def __str__(self):
        return f'Cliente: {self.cliente}\nDia de inicio: {self.dia_inicio}\nDia final: {self.dia_fim}\n---\nQuarto: \n{self.quarto}\n---\nStatus: {self.status}' 
    
    def __repr__(self):
        return f'Quarto({self.dia_inicio},{self.dia_fim},{self.cliente},{self.quarto},{self.status})'
    
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
        serialized_string = "{}/{}/{}/{}/{}".format(self.dia_inicio, self.dia_fim, self.cliente, self.quarto.numero, self.status)
        return serialized_string

    def deserializar(self, string, quartos):
        split_string = string.strip().split("/")
        split_string[0] #dia inicio
        split_string[1] #dia fim
        split_string[2] #cliente
        split_string[3] #numero do quarto
        split_string[4] #status
        
        self.dia_inicio = split_string[0]
        self.dia_fim = split_string[1]
        self.cliente = split_string[2]
        for i in quartos:
            if i.numero == split_string[3]:
                self.quarto = i
                break
        self.status = split_string[4]
        return self