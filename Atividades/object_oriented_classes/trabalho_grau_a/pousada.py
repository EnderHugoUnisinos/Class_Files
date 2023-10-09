from reserva import Reserva 
from quarto import Quarto
from produto import Produto
from utils import Utils

class Pousada:
    def __init__ (self, nome = "", contato = "", quartos = [], reservas = [], produtos = []):
        self.nome = nome
        self.contato = contato
        self.quartos = quartos
        self.reservas = reservas
        self.produtos = produtos

    def getNome(self):
        return self.nome
    def getContato(self):
        return self.contato
    def getQuartos(self):
        return self.quartos
    def getReservas(self):
        return self.reservas
    def getProdutos(self):
        return self.produtos
    
    def setNome(self, nome):
        self.nome = nome
    def setContato(self, contato):
        self.contato = contato
    def setQuartos(self, quartos):
        self.quartos = quartos
    def setReservas(self, reservas):
        self.reservas = reservas
    def setProdutos(self, produtos):
        self.produtos = produtos

    def appendQuartos(self, quarto):
        self.quartos.append(quarto)
    def appendReservas(self, reserva):
        self.reservas.append(reserva)
    def appendProdutos(self, produto):
        self.produtos.append(produto)
    
    def popQuartos(self, index):
        self.quartos.pop(index)
    def popProdutos(self, index):
        self.produtos.pop(index)

    def adicionarQuarto(self, quartoString):
        self.appendQuartos(Quarto().deserializar(quartoString))
    def removerQuarto(self, numero):
        quartos = self.getQuartos()
        for id, i in enumerate(quartos):
            if int(i.getNumero()) == numero:
                self.popQuartos(id)

    def adicionarProduto(self, produtoString):
        self.appendProdutos(Produto().deserializar(produtoString))
    def removerProduto(self, codigo):
        produtos = self.getProdutos()
        for id, i in enumerate(produtos):
            if int(i.getNumero()) == int(codigo):
                self.popProdutos(id)

    def carregaDados(self, pousadaString, quartoStrings, reservaStrings, produtoStrings):
        self.deserializar(pousadaString[0])

        for i in quartoStrings:
           self.appendQuartos(Quarto().deserializar(i))
        
        for i in reservaStrings:
            self.appendReservas(Reserva().deserializar(i, self.getQuartos()))

        for i in produtoStrings:
            self.appendProdutos(Produto().deserializar(i))
    def salvaDados(self):
        dadosDict = {"pousada":[],"quartos":[],"reservas":[],"produtos":[]}

        dadosDict["pousada"].append(self.serializar())

        for i in self.getQuartos():
            dadosDict["quartos"].append(i.serializar())

        for i in self.getReservas():
            if i.getStatus() not in ["O","C"]:
                dadosDict["reservas"].append(i.serializar())
            #skip to the next loop

        for i in self.getProdutos():
            dadosDict["produtos"].append(i.serializar())
        
        return dadosDict

    def consultaDisponibilidade(self, data, quarto):
        quartoFound = None
        reservaCount = 0
        if self.getReservas() != []:
            for i in self.getReservas():
                if int(i.getQuarto().getNumero()) == int(quarto):
                    reservaCount += 1
                    if not Utils().checkDateOverlap(i.getDatas(), data):
                        quartoFound = i.getQuarto()
        if reservaCount == 0:
            quartoFound = self.searchForQuarto(quarto)
        return quartoFound
    def consultaReserva(self, data, cliente, quarto):
        reserva = []
        if self.getReservas()[0] != None:
            for i in self.getReservas():
                if (i.getCliente() == cliente or cliente == None) and (i.getQuarto() == self.searchForQuarto(quarto) or quarto == None) and (data in i.getDatas() or data == None):
                    reserva.append(i)
        return reserva
    def realizaReserva(self, diaInicio, diaFim, cliente, quarto):
        self.appendReservas(Reserva(diaInicio,diaFim,cliente,quarto))
    def cancelaReserva(self, cliente):
        modified = 0
        if self.getReservas()[0] != None:
            for i in self.getReservas():
                if i.getCliente() == cliente:
                    i.setStatus("C")
                    modified += 1
        return modified
    def realizarCheckOut(self, cliente):
        modified = 0
        for i in cliente:
            i.setStatus("O")
            i.getQuarto().limpaConsumo()
            modified += 1
        return modified
    def realizarCheckIn(self, cliente):
        modified = 0
        for i in cliente:
            i.setStatus("I")
            modified += 1
        return modified

    def searchForReservas(self, cliente):
        listaReservas = []
        if self.getReservas()[0] != None:
            for i in self.getReservas():
                if i.getCliente() == cliente:
                    listaReservas.append(i)
        return listaReservas
    def searchForQuarto(self, numero):
        result = None
        for i in self.getQuartos():
            if i.numero == numero:
                result = i
        return result

    def serializar(self):
        serializedString = "{};{};".format(self.getNome(),self.getContato())
        return serializedString
    def deserializar(self, string):
        splitString = string.strip().split(";")
        splitString[0] #nome
        splitString[1] #contato
        
        self.setNome(splitString[0])
        self.setContato(splitString[1])
        
    def organizarListas(self):
        self.setQuartos(sorted(self.getQuartos(), key=lambda x: x.getNumero()))
        self.setReservas(sorted(self.getReservas(), key=lambda x: Utils().convertStringToDate(x.getDatas()[0])))
        self.setProdutos(sorted(self.getProdutos(), key=lambda x: x.getCodigo()))