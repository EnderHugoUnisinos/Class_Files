from reserva import Reserva 
from quarto import Quarto
from produto import Produto
from utils import Utils

class Pousada:
    def __init__ (self,nome, contato, quartos = [], reservas = [], produtos = []):
        self.nome = nome
        self.contato = contato
        self.quartos = quartos
        self.reservas = reservas
        self.produtos = produtos
        self.utils = Utils()

    def carregarDados(self):
        pass

    def salvarDados(self):
        pass

    def consultaDisponibilidade(self, data, quarto):
        reserva = None
        if self.reservas[0] != None:
            for i in self.reservas:
                if i.get_quarto() == quarto and self.utils.verificar_data_overlap(i.get_data(), data) == False:
                    reserva = i
        return reserva

    def consultaReserva(self, data, cliente, quarto):
        reserva = None
        if self.reservas[0] != None:
            for i in self.reservas:
                if i.get_cliente() == cliente and i.get_quarto() == quarto and i.get_data() == data:
                    reserva = i
        return reserva

    def realizaReserva(self, datas, cliente, quarto):
        self.reservas.append(Reserva(datas[0],datas[1],cliente,quarto))

    def cancelaReserva(self, cliente):
        modified = 0
        if self.reservas[0] != None:
            for i in self.reservas:
                if i.get_cliente() == cliente:
                    i.set_status("C")
                    modified += 1
        return modified

    def realizarCheckin(self, cliente):
        modified = 0
        if self.reservas[0] != None:
            for i in self.reservas:
                if i.get_cliente() == cliente:
                    i.set_status("I")
                    modified += 1
        return modified

    def realizarCheckOut(self, cliente):
        modified = 0
        if self.reservas[0] != None:
            for i in self.reservas:
                if i.get_cliente() == cliente:
                    i.set_status("O")
                    modified += 1
        return modified

    def serializar(self):
        serialized_string = "{};{};".format(self.nome,self.contato)
        return serialized_string
    
    def deserializar(self, string):
        split_string = string.strip().split(";")
        split_string[0] #nome
        split_string[1] #contato