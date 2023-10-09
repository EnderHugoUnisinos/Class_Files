from pousada import Pousada
from utils import Utils

class SystemModel:
    def __init__(self, pousadaPath, produtoPath, quartoPath, reservaPath) -> None:
        self.pousadaPath = pousadaPath
        self.produtoPath = produtoPath
        self.quartoPath = quartoPath
        self.reservaPath = reservaPath
        self.pousada = Pousada()
    
    def getPaths(self):
        return [self.pousadaPath, self.produtoPath, self.quartoPath, self.reservaPath]
    def getPousada(self):
        return self.pousada

    def salvarDados(self):
        dadosDict = self.pousada.salvaDados()
        paths = self.getPaths()
        self.writeToFile(dadosDict["pousada"], paths[0])
        self.writeToFile(dadosDict["produtos"], paths[1])
        self.writeToFile(dadosDict["quartos"], paths[2])
        self.writeToFile(dadosDict["reservas"], paths[3])
    def carregarDados(self):
        paths = self.getPaths()
        pousadaString = self.readFromFile(paths[0])
        produtoStrings = self.readFromFile(paths[1])
        quartoStrings = self.readFromFile(paths[2])
        reservaStrings = self.readFromFile(paths[3])
        self.getPousada().carregaDados(pousadaString, quartoStrings, reservaStrings, produtoStrings)
    
    def realizarCheckIn(self, reservas):
        self.getPousada().realizarCheckIn(reservas)
    def realizarCheckOut(self, reservas):
        return self.getPousada().realizarCheckOut(reservas)
    def searchForReservas(self, cliente):
        return self.getPousada().searchForReservas(cliente)
    def cancelarReserva(self, cliente):
        self.getPousada().cancelaReserva(cliente)
    def realizarReserva(self, dados):
        self.getPousada().realizaReserva(dados["diaInicio"],dados["diaFim"],dados["cliente"],self.getPousada().searchForQuarto(dados["quarto"]))
    def consultarDisponibilidade(self, data, quarto):
        return self.getPousada().consultaDisponibilidade(data, quarto)   
    def consultarReserva(self, data, cliente, quarto):
        return self.getPousada().consultaReserva(data, cliente, quarto)

    def adicionarQuarto(self, quarto):
        self.pousada.adicionarQuarto(quarto)
    def removerQuarto(self, numero):
        self.pousada.removerQuarto(numero)
    def adicionarMultiplosQuartos(self, lista):
        for i in lista:
            self.pousada.adicionarQuarto(i)
    def removerMultiplosQuartos(self, lista):
        for i in lista:
            self.pousada.removerQuarto(i)

    def adicionarProduto(self, produto):
        self.pousada.adicionarProduto(produto)
    def removerProduto(self, produto):
        self.pousada.removerProduto(produto)
    def adicionarMultiplosProdutos(self, lista):
        for i in lista:
            self.pousada.adicionarProduto(i)
    def removerMultiplosProdutos(self, lista):
        for i in lista:
            self.pousada.removerProduto(i)

    def registrarConsumo(self, cliente, consumo):
        modified = 0
        for i in self.searchForReservas(cliente):
            quarto = i.getQuarto()
            for j in consumo:
                quarto.adicionaConsumo(j)
                modified += 1
        return modified
    
    def getProdutos(self):
        produtos = self.getPousada().getProdutos()
        return produtos
    def getQuartos(self):
        quartos = self.getPousada().getQuartos()
        return quartos
    def getReservas(self):
        reservas = self.getPousada().getReservas()
        return reservas

    def writeToFile(self, stringList, path):
        try:
            with open(path, "w") as file:
                file.writelines(line + "\n" for line in stringList)
            return True
        except: 
            return False   
    def readFromFile(self, path):
        try:
            with open(path, "r") as file:
                string = file.readlines()
            return string
        except:
            return False

    def organizarListas(self):
        self.getPousada().organizarListas()