from reserva import Reserva 
from quarto import Quarto

class Pousada:
    def __init__ (self, nome, contato, quartos, reservas = [], produtos = []):
        self.nome = nome
        self.contato = contato
        self.quartos = quartos
        self.reservas = reservas
        self.produtos = produtos

    def carregarDados(self):
        pass

    def salvarDados(self):
        pass

    def consultaDisponibilidade(self, data, quarto):
        pass

    def consultaReserva(self, data, cliente, quarto):
        pass

    def realizaReserva(self, datas, cliente, quarto):
        self.reservas.append(Reserva(datas[0],datas[1],cliente,quarto))

    def cancelaReserva(self, cliente):
        pass

    def realizarCheckin(self, cliente):
        pass

    def realizarCheckOut(self, cliente):
        pass
