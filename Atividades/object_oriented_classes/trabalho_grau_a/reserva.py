class Reserva:
    def __init__ (self, dia_inicio, dia_fim, cliente, quarto, status = 'A'):
        self.dia_inicio = dia_inicio
        self.dia_fim = dia_fim
        self.cliente = cliente
        self.quarto = quarto
        self.status = status