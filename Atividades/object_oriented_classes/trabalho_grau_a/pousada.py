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


    def get_nome(self):
        return self.nome
    def get_contato(self):
        return self.contato
    def get_quartos(self):
        return self.quartos
    def get_reservas(self):
        return self.reservas
    def get_produtos(self):
        return self.produtos
    
    def set_nome(self, nome):
        self.nome = nome
    def set_contato(self, contato):
        self.contato = contato
    def set_quartos(self, quartos):
        self.quartos = quartos
    def set_reservas(self, reservas):
        self.reservas = reservas
    def set_produtos(self, produtos):
        self.produtos = produtos

    def append_quartos(self, quarto):
        self.quartos.append(quarto)
    def append_reservas(self, reserva):
        self.reservas.append(reserva)
    def append_produtos(self, produto):
        self.produtos.append(produto)
    
    def pop_quartos(self, index):
        self.quartos.pop(index)
    def pop_produtos(self, index):
        self.produtos.pop(index)

    def adicionar_quarto(self, quarto_string):
        self.append_quartos(Quarto().deserializar(quarto_string))
    def remover_quarto(self, numero):
        quartos = self.get_quartos()
        for id, i in enumerate(quartos):
            if int(i.get_numero()) == numero:
                self.pop_quartos(id)

    def adicionar_produto(self, produto_string):
        self.append_produtos(Produto().deserializar(produto_string))
    def remover_produto(self, codigo):
        produtos = self.get_produtos()
        for id, i in enumerate(produtos):
            if int(i.get_numero()) == int(codigo):
                self.pop_produtos(id)

    def carregar_dados(self, pousadaString, quartoStrings, reservaStrings, produtoStrings):
        self.deserializar(pousadaString[0])

        for i in quartoStrings:
           self.append_quartos(Quarto().deserializar(i))
        
        for i in reservaStrings:
            self.append_reservas(Reserva().deserializar(i, self.get_quartos()))

        for i in produtoStrings:
            self.append_produtos(Produto().deserializar(i))
    def salvar_dados(self):
        dadosDict = {"pousada":[],"quartos":[],"reservas":[],"produtos":[]}

        dadosDict["pousada"].append(self.serializar())

        for i in self.get_quartos():
            dadosDict["quartos"].append(i.serializar())

        for i in self.get_reservas():
            if i.get_status() not in ["O","C"]:
                dadosDict["reservas"].append(i.serializar())
            #skip to the next loop

        for i in self.get_produtos():
            dadosDict["produtos"].append(i.serializar())
        
        return dadosDict

    def consulta_disponibilidade(self, data, numero):
        quarto = None
        reservaCount = 0
        if self.get_reservas() != []:
            for i in self.get_reservas():
                if i.get_quarto().get_numero() == numero:
                    reservaCount += 1
                    if not Utils().check_date_overlap(i.get_datas(), data):
                        quarto = i.get_quarto()
        if reservaCount == 0:
            quarto = self.search_for_quarto(numero)
        return quarto
    def consulta_reserva(self, data, cliente, numero):
        reserva = []
        if self.get_reservas()[0] != None:
            for i in self.get_reservas():
                if (i.get_cliente() == cliente or cliente == None) and (i.get_quarto() == self.search_for_quarto(numero) or numero == None) and (i.get_datas() == data or data == None):
                    reserva.append(i)
        return reserva
    def realiza_reserva(self, dia_inicio, dia_fim, cliente, quarto):
        self.append_reservas(Reserva(dia_inicio,dia_fim,cliente,quarto))
    def cancela_reserva(self, cliente):
        modified = 0
        if self.get_reservas()[0] != None:
            for i in self.get_reservas():
                if i.get_cliente() == cliente:
                    i.set_status("C")
                    modified += 1
        return modified
    def realizar_check_out(self, reservas):
        modified = 0
        for i in reservas:
            i.set_status("O")
            i.get_quarto().limpa_consumo()
            modified += 1
        return modified
    def realizar_check_in(self, reservas):
        modified = 0
        for i in reservas:
            i.set_status("I")
            modified += 1
        return modified

    def search_for_reservas(self, cliente):
        lista_reservas = []
        if self.get_reservas()[0] != None:
            for i in self.get_reservas():
                if i.get_cliente() == cliente:
                    lista_reservas.append(i)
        return lista_reservas
    def search_for_quarto(self, numero):
        result = None
        for i in self.get_quartos():
            if i.numero == numero:
                result = i
        return result

    def serializar(self):
        serialized_string = "{};{};".format(self.get_nome(),self.get_contato())
        return serialized_string
    def deserializar(self, string):
        split_string = string.strip().split(";")
        split_string[0] #nome
        split_string[1] #contato
        
        self.set_nome(split_string[0])
        self.set_contato(split_string[1])
        
    def organizar_listas(self):
        self.set_quartos(sorted(self.get_quartos(), key=lambda x: x.get_numero()))
        self.set_reservas(sorted(self.get_reservas(), key=lambda x: Utils().convert_string_to_date(x.get_datas()[0])))
        self.set_produtos(sorted(self.get_produtos(), key=lambda x: x.get_codigo()))