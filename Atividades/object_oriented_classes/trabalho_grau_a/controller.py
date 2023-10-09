from view import SystemView
from model import SystemModel   
from utils import Utils

class SystemController:
    def __init__(self) -> None:
        self.view = SystemView()
        self.model= SystemModel("assets/pousada.txt","assets/produto.txt","assets/quarto.txt","assets/reserva.txt")
        self.model.carregarDados()

    def menuPrincipal(self):
        while True:
            userInput = self.view.menuPrincipal()
            match userInput:
                case "0":
                    self.sairSistema()
                case "1":
                    self.consultarDisponibilidade()
                case "2":
                    self.consultarReserva()
                case "3":
                    self.realizarReserva()          
                case "4":
                    self.cancelarReserva()
                case "5":
                    self.realizarCheckIn()
                case "6":
                    self.realizarCheckOut()
                case "7":
                    self.registrarConsumo()
                case "8":
                    self.view.clearConsole()
                    self.menuQuartos()
                case "9":
                    self.view.clearConsole()
                    self.menuProdutos()
                case "10":
                    self.salvarDados()
                case default:
                    self.view.errorMessage("Numero inserido invalido","Insira um numero presente no menu (0 - 9)")
            self.view.awaitInput()
            self.organizarListas()
        
    def sairSistema(self):
        self.salvarDados()
        quit()
    def consultarDisponibilidade(self):
        userInput = self.view.consultarDisponibilidade()
        result = self.model.consultarDisponibilidade(userInput["data"], userInput["quarto"])
        self.view.clearConsole()
        #Testa se a consulta retornou algo
        if result != None:
            self.view.printData(str(result))
        else:
            self.view.printData("Quarto indisponivel.")
    def consultarReserva(self):
        produtos = self.model.getProdutos()
        quartos = self.model.getQuartos()
        userInput = self.view.consultarReserva(quartos)
        result = self.model.consultarReserva(userInput["data"],userInput["cliente"],userInput["quarto"])
        self.view.clearConsole()
        if result != []:
            self.view.displayReservas(result, produtos)
        else:
            self.view.errorMessage("Reserva não encontrada.","Verifique se os dados inseridos estão corretos")
    def realizarReserva(self):
        quartos = self.model.getQuartos()
        userInput = self.view.realizarReserva(quartos)
        resultA = self.model.consultarDisponibilidade(userInput["diaInicio"], userInput["quarto"])
        resultB = self.model.consultarDisponibilidade(userInput["diaFim"], userInput["quarto"])
        self.view.clearConsole()
        #Testa se a consulta retornou algo
        if all(v is not None for v in [resultA, resultB]):
            #try:
            reservaExistente = self.model.consultarReserva(None, userInput["cliente"], None)
            if all(v.getStatus().upper() not in ["A","I"] for v in reservaExistente):
                self.model.realizarReserva(userInput)
                self.view.successMessage("Reserva realizada com sucesso")
            else:
                self.view.errorMessage("Cliente já tem uma reserva ativa", "Certifique-se que o cliente realizou check-out/cancelou a reserva antiga")
            #except:
                #self.view.errorMessage("Ocorreu um erro ao inserir a reserva","Entre em contato com o desenvolvedor")
        else:
            self.view.printData("Quarto indisponivel.")     
    def cancelarReserva(self):
        userInput = self.view.cancelarReserva()
        result = self.model.consultarReserva(None, userInput, None)
        self.view.clearConsole()
        #Testa se a consulta retornou algo
        if result[0] != None:
            try:
                self.model.cancelarReserva(userInput)
                self.view.successMessage("Reserva cancelada com sucesso")
            except:
                self.view.errorMessage("Ocorreu um erro ao cancelar a reserva","Entre em contato com o desenvolvedor")
        else:
            self.view.printData("Nenhuma reserva encontrada.")  
    def realizarCheckIn(self):
        produtos = self.model.getProdutos()
        userInput = self.view.realizarCheckin()
        result = self.model.searchForReservas(userInput)
        self.view.clearConsole()
        if result != None:
            self.view.displayReservas(result, produtos)
            self.model.realizarCheckIn(result)
        else: 
            self.view.errorMessage("Reserva não encontrada.","Verifique se os dados inseridos estão corretos")
    def realizarCheckOut(self):
        produtos = self.model.getProdutos()
        userInput = self.view.realizarCheckout()
        result = self.model.searchForReservas(userInput)
        self.view.clearConsole()
        if result != None:
            self.view.displayReservas(result, produtos)
            self.model.realizarCheckOut(result)
        else:
            self.view.errorMessage("Reserva não encontrada.","Verifique se os dados inseridos estão corretos")
    def registrarConsumo(self):
        produtos = self.model.getProdutos()
        userInput = self.view.registrarConsumo(produtos)
        self.model.registrarConsumo(userInput["cliente"],userInput["consumo"])
    def salvarDados(self):
        self.model.salvarDados()
        self.model.carregarDados()
    def menuQuartos(self):
        while True:
            userInput = self.view.menuQuartos()
            match userInput:
                case "0":
                    break
                case "1":
                    self.adicionarQuarto()
                case "2":
                    self.removerQuarto()
                case "3":
                    self.adicionarMultiplosQuartos()
                case "4":
                    self.removerMultiplosQuartos()
                case "5":
                    self.listarQuartos()
                case default:
                    self.view.errorMessage("Numero inserido invalido","Insira um numero presente no menu (0 - 5)")
            self.view.awaitInput()
            self.organizarListas()

    def adicionarQuarto(self):
        quartos = self.model.getQuartos()
        userInput = self.view.adicionarQuarto(quartos)
        self.model.adicionarQuarto(userInput)
    def removerQuarto(self):
        quartos = self.model.getQuartos()
        userInput = self.view.removerQuarto(quartos)
        result = self.model.consultarReserva(None, None, userInput)
        if result == None:
            self.model.removerQuarto(userInput)
        else:
            self.view.errorMessage("Quarto inserido está reservado","Cancele a reserva antes de remover")
    def adicionarMultiplosQuartos(self):
        quartos = self.model.getQuartos()
        userInputList = self.view.adicionarMultiplosQuartos(quartos)
        self.model.adicionarMultiplosQuartos(userInputList)
    def removerMultiplosQuartos(self):
        quartos = self.model.getQuartos()
        userInputList = self.view.removerMultiplosQuartos(quartos)
        if all(v is None for v in userInputList):
            self.model.removerMultiplosQuartos(userInputList)
        else:
            self.view.errorMessage("Um dos quartos inseridos está reservado","Cancele a reserva antes de remover")
    def listarQuartos(self):
        quartos = self.model.getQuartos()
        self.view.displayQuartos(quartos)

    def menuProdutos(self):
        while True:
            userInput = self.view.menuProdutos()
            match userInput:
                case "0":
                    break
                case "1":
                    self.adicionarProduto()
                case "2":
                    self.removerProduto()
                case "3":
                    self.listarProdutos()
                case default:
                    self.view.errorMessage("Numero inserido invalido","Insira um numero presente no menu (0 - 4)")
            self.view.awaitInput()
            self.organizarListas()
        
    def adicionarProduto(self):
        produtos = self.model.getProdutos()
        userInput = self.view.adicionarProduto(produtos)
        self.model.adicionarProduto(userInput)
    def removerProduto(self):
        produtos = self.model.getProdutos()
        userInput = self.view.removerProduto(produtos)
        self.model.removerProduto(userInput)
    def adicionarMultiplosProdutos(self):
        produtos = self.model.getProdutos()
        userInputList = self.view.adicionarMultiplosProdutos(produtos)
        self.model.adicionarMultiplosProdutos(userInputList)
    def removerMultiplosProdutos(self):
        produtos = self.model.getProdutos()
        userInputList = self.view.removerMultiplosProdutos(produtos)
        self.model.removerMultiplosProdutos(userInputList)
    def listarProdutos(self):
        produtos = self.model.getProdutos()
        self.view.displayProdutos(produtos)

    def organizarListas(self):
        self.model.organizarListas()