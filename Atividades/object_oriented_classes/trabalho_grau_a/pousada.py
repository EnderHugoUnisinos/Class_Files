from reserva import Reserva 
from quarto import Quarto
from produto import Produto
from utils import Utils

class Pousada:
    def __init__ (self,nome = "", contato = "", quartos = [], reservas = [], produtos = []):
        self.nome = nome
        self.contato = contato
        self.quartos = quartos
        self.reservas = reservas
        self.produtos = produtos
        self.utils = Utils()

    def carregarDados(self, pousadaString, quartoStrings, reservaStrings, produtoStrings):
       
        self.deserializar(pousadaString[0])

        for i in quartoStrings:
           self.quartos.append(Quarto().deserializar(i))
        
        for i in reservaStrings:
            self.reservas.append(Reserva().deserializar(i, self.quartos))

        for i in produtoStrings:
            self.produtos.append(Produto().deserializar(i))

    def salvarDados(self):
        dadosDict = {"pousada":[],"quarto":[],"reserva":[],"produto":[]}

        dadosDict["pousada"].append(self.serializar)

        for i in self.quartos:
            dadosDict["quartos"].append(i.serializar())

        for i in self.reservas:
            dadosDict["reservas"].append(i.serializar())

        for i in self.produtos:
            dadosDict["produtos"].append(i.serializar())
        
        return dadosDict

    def consultaDisponibilidade(self, data, numero):
        quarto = None
        reservaCount = 0
        if self.reservas != []:
            for i in self.reservas:
                if i.get_quarto().numero == numero:
                    reservaCount += 1
                    if not self.utils.verificar_data_overlap(i.get_data(), data):
                        quarto = i.get_quarto()
        if reservaCount == 0:
            quarto = self.searchQuarto(numero)
        return quarto

    def consultaReserva(self, data, cliente, numero):
        reserva = []
        if self.reservas[0] != None:
            for i in self.reservas:
                if (i.get_cliente() == cliente or cliente == None) and (i.get_quarto() == self.searchQuarto(numero) or numero == None) and (i.get_data() == data or data == None):
                    reserva.append(i)
        return reserva

    def realizaReserva(self, dia_inicio, dia_fim, cliente, quarto):
        self.reservas.append(Reserva(dia_inicio,dia_fim,cliente,quarto))

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

    def searchQuarto(self, numero):
        result = None
        for i in self.quartos:
            if i.numero == numero:
                result = i
        return result

    def serializar(self):
        serialized_string = "{};{};".format(self.nome,self.contato)
        return serialized_string
    
    def deserializar(self, string):
        split_string = string.strip().split(";")
        split_string[0] #nome
        split_string[1] #contato
        
        self.nome = split_string[0]
        self.contato = split_string[1]
        