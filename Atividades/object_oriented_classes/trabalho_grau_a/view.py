from utils import Utils
import os
class SystemView:
    def __init__(self) -> None:
        pass

    def menuPrincipal(self):
        print("[1] : Consultar disponibilidade")
        print("[2] : Consultar reserva")
        print("[3] : Realizar reserva")
        print("[4] : Cancelar reserva")
        print("[5] : Realizar check-in")
        print("[6] : Realizar check-out")
        print("[7] : Registrar consumo")
        print("[8] : Quartos")
        print("[9] : Produtos")
        print("[10] : Salvar")
        print("[0] : Sair")
        userInput = input("Insira a opção desejada: ")
        return userInput
    def consultarDisponibilidade(self):
        userInput = {"data":"","quarto":""}
        
        while True:
            quartoPrevalid = input("Insira o numero do quarto que deseja consultar: ")
            if not Utils().isValidNumberFormat(quartoPrevalid):
                self.errorMessage("Formato de numero incorreto", "Insira um numero de quarto seguindo o padrão: 101, 102, 201...")
            else:
                break
        userInput["quarto"] = quartoPrevalid
        
        while True:
            dataPrevalid = input("Insira a data no padrão DD-MM-AAAA: ")
            if not Utils().isValidDateFormat(dataPrevalid):
                self.errorMessage("Formato de data incorreto", "Insira uma data seguindo o padrão: DD-MM-AAAA")
            else:
                break
        userInput["data"] = dataPrevalid
        
        return userInput
    def consultarReserva(self, quartos):
        userInput = {"cliente":"","data":"","quarto":""}
        
        print("Para cada campo insira os parametros pedidos ou insira \"X\" para não utilizar o parametro")
        self.awaitInput()
        
        clientePrevalid = input("Insira o nome do cliente da reserva que deseja consultar: ")
        if clientePrevalid.upper() == "X":
            userInput["cliente"] = None
        else:
            userInput["cliente"] = clientePrevalid
        
        while True:
            quartoPrevalid = input("Insira o numero do quarto da reserva que deseja consultar: ")
            if not Utils().isValidRoomNumber(quartoPrevalid, quartos) and quartoPrevalid.upper() != "X":
                self.errorMessage("Formato de numero incorreto", "Insira um numero de quarto seguindo o padrão: 101, 102, 201...")
            else:
                break
        if quartoPrevalid.upper() == "X":
            userInput["quarto"] = None
        else:
            userInput["quarto"] = quartoPrevalid
        
        while True:
            dataPrevalid = input("Insira a data da reserva que deseja consultar no padrão DD-MM-AAAA: ")
            if not Utils().isValidDateFormat(dataPrevalid) and dataPrevalid.upper() != "X":
                self.errorMessage("Formato de data incorreto", "Insira uma data seguindo o padrão: DD-MM-AAAA")
            else:
                break
        if dataPrevalid.upper() == "X":
            userInput["data"] = None
        else:
            userInput["data"] = dataPrevalid
        
        return userInput
    def realizarReserva(self, quartos):
        userInput = {"diaInicio":"", "diaFim":"","cliente":"","quarto":""}
        userInput["cliente"] = input("Insira o nome do cliente: ")
        
        while True:
            quartoPrevalid = input("Insira o numero do quarto: ")
            if not Utils().isValidRoomNumber(quartoPrevalid, quartos):
                self.errorMessage("Formato de numero incorreto", "Insira um numero de quarto seguindo o padrão: 101, 102, 201...")
            else:
                break
        userInput["quarto"] = quartoPrevalid
        
        while True:
            dataPrevalid = input("Insira o dia de inicio no padrão DD-MM-AAAA: ")
            if not Utils().isValidDateFormat(dataPrevalid):
                self.errorMessage("Formato de data incorreto", "Insira uma data seguindo o padrão: DD-MM-AAAA")
            else:
                break
        userInput["diaInicio"] = dataPrevalid
        
        while True:
            dataPrevalid = input("Insira o dia final no padrão DD-MM-AAAA: ")
            if not Utils().isValidDateFormat(dataPrevalid):
                self.errorMessage("Formato de data incorreto", "Insira uma data seguindo o padrão: DD-MM-AAAA")
            else:
                break
        userInput["diaFim"] = dataPrevalid
        
        return userInput
    def cancelarReserva(self):
        userInput = input("Insira o nome do cliente da reserva que deseja cancelar: ")
        return userInput
    def realizarCheckin(self):
        userInput = input("Insira o nome do cliente da reserva que deseja realizar check-in: ")
        return userInput 
    def realizarCheckout(self):
        userInput = input("Insira o nome do cliente da reserva que deseja realizar check-out: ")
        return userInput 
    def registrarConsumo(self, produtos):
        userInput = {"cliente":"","consumo":[]}
        
        userInput["cliente"] = input("Insira o nome do cliente cujo consumo deseja reservar: ")
        
        self.displayProdutos(produtos)
        rawInput = ""
        while rawInput != "X":
            rawInput = input("Insira o codigo dos produtos a registrar (um de cada vez), digite \"X\" para encerrar o registro:")
            if rawInput != "X" and Utils().isValidProductCode(rawInput, produtos) and rawInput.strip() != "":
                userInput["consumo"].append(rawInput)
        return userInput
    
    def menuQuartos(self):
        print("[1] : Adicionar quarto")
        print("[2] : Remover quarto")
        print("[3] : Adicionar multiplos quartos")
        print("[4] : Remover multiplos quartos")
        print("[5] : Listar quartos")
        print("[0] : Voltar ao menu principal")
        userInput = input("Insira a opção desejada: ")
        return userInput
    def adicionarQuarto(self, quartos):
        userInput = {"numero":"","categoria":"","diaria":""}
        rawInput = ""
        while not Utils().isValidNumberFormat(rawInput) or Utils.isValidRoomNumber(rawInput, quartos):
            rawInput = input("Insira o numero do quarto:")
            if not Utils().isValidNumberFormat(rawInput) or Utils.isValidRoomNumber(rawInput, quartos):
                self.errorMessage("Quarto inserido invalido","Verifique se o quarto já existe")
        userInput["numero"] = rawInput
        while not Utils().isValidCategory(rawInput):
            rawInput = input("Insira a categoria do quarto (S/M/P):")
            if not Utils().isValidCategory(rawInput):
                self.errorMessage("Categoria inserida invalida","Verifique se a categoria existe (S/M/P)")
        userInput["categoria"] = rawInput
        while not Utils().isValidPrice(rawInput):
            rawInput = input("Insira a diaria do quarto:")
            if not Utils().isValidPrice(rawInput):
                self.errorMessage("Valor inserido invalido","Verifique se o que foi inserido é um valor numerico valido")
        userInput["diaria"] = rawInput
        userInput = f"{userInput['numero']}/{userInput['categoria']}/{userInput['diaria']}"
        return userInput
    def removerQuarto(self, quartos):
        rawInput = ""
        while not Utils().isValidRoomNumber(rawInput, quartos):
            rawInput = input("Insira o numero do quarto que deseja remover:")
        userInput = rawInput
        return userInput
    def adicionarMultiplosQuartos(self, quartos):
        rawInput = "None"
        print("Insira os dados no padrão seguinte: numero/categoria/diaria")
        print("Ex: \"101/S/80\"")
        self.awaitInput()
        userInput = []
        while rawInput.upper() != "X":
            rawInput = input("Insira os dados do quarto, insira X para encerrar: ")
            try:
                numero, categoria, diaria = rawInput.split("/")
                if Utils().isValidNumberFormat(numero) and not Utils.isValidRoomNumber(numero, quartos) and Utils().isValidCategory(categoria) and Utils.isValidPrice(diaria):
                    userInput.append(rawInput)
                elif rawInput.upper() != "X":
                    self.errorMessage("Dados não puderam ser validados","Siga o padrão numero/categoria/diaria")
            except:
                self.errorMessage("Dados separados incorretamente", "Siga o padrão numero/categoria/diaria")
        return userInput
    def removerMultiplosQuartos(self, quartos):
        rawInput = ""
        userInput = []
        while rawInput.upper() != "X":
            rawInput = input("Insira o numero do quarto, insira X para encerrar: ")
            if Utils().isValidRoomNumber(rawInput, quartos):
                userInput.append(int(rawInput))
            elif rawInput.upper() != "X":
                self.errorMessage("Não foi possivel validar o numero do quarto","Verifique o valor inserido")
        return userInput

    def menuProdutos(self):
        print("[1] : Adicionar produto")
        print("[2] : Remover produto")
        print("[3] : Adicionar multiplos produtos")
        print("[4] : Remover multiplos produtos")
        print("[5] : Listar produtos")
        print("[0] : Voltar ao menu principal")
        userInput = input("Insira a opção desejada: ")
        return userInput
    def adicionarProduto(self, produtos):
        userInput = {"codigo":"","nome":"","preco":""}
        rawInput = ""

        while not Utils().isValidCodeFormat(rawInput) or Utils().isValidProductCode(rawInput, produtos):
            rawInput = input("Insira o codigo do produto:")
            if not Utils().isValidCodeFormat(rawInput) or Utils().isValidProductCode(rawInput, produtos):
                self.errorMessage("codigo inserido invalido","Verifique se o produto já existe")
        userInput["codigo"] = rawInput

        rawInput = input("Insira o nome do produto:")
        userInput["nome"] = rawInput

        while not Utils().isValidPrice(rawInput):
            rawInput = input("Insira o preco do quarto:")
            if not Utils().isValidPrice(rawInput):
                self.errorMessage("Valor inserido invalido","Verifique se o que foi inserido é um valor numerico valido")
        userInput["preco"] = rawInput
        userInput = f"{userInput['codigo']}/{userInput['nome']}/{userInput['preco']}"
        return userInput
    def removerProduto(self, produtos):
        rawInput = ""
        while not Utils().isValidProductCode(rawInput, produtos) and rawInput != "000":
            rawInput = input("Insira o codigo do produto que deseja remover:")
        userInput = rawInput
        return userInput
    def adicionarMultiplosProdutos(self, produtos):
        rawInput = "None"
        print("Insira os dados no padrão seguinte: codigo/nome/preço")
        print("Ex: \"001/Jantar de Bife/49.99\"")
        self.awaitInput()
        userInput = []
        while rawInput.upper() != "X":
            rawInput = input("Insira os dados do produto, insira X para encerrar: ")
            try:
                codigo, nome, preco = rawInput.split("/")
                if Utils().isValidNumberFormat(codigo) and not Utils().isValidProductCode(codigo, produtos) and Utils().isValidPrice(preco):
                    userInput.append(rawInput)
                elif rawInput.upper() != "X":
                    self.errorMessage("Dados não puderam ser validados","Siga o padrão codigo/nome/preço")
            except:
                self.errorMessage("Dados separados incorretamente", "Siga o padrão codigo/nome/preço")
        return userInput
    def removerMultiplosProdutos(self, produtos):
        rawInput = ""
        userInput = []
        while rawInput.upper() != "X":
            rawInput = input("Insira o numero do produto, insira X para encerrar: ")
            if Utils().isValidProductCode(rawInput, produtos):
                userInput.append(int(rawInput))
            elif rawInput.upper() != "X":
                self.errorMessage("Não foi possivel validar o codigo do produto","Verifique o valor inserido")
        return userInput

    
    def displayProdutos(self, produtos):
        for i in produtos:
            print(f"{i}")
    def displayReservas(self, reservas, produtos):
        for i in reservas:
            total = i.calcularDiaria()
            for j in i.getQuarto().listaConsumo(produtos):
                total += j.getPreco()
            print(f"\nReserva\n{i}")
            print(f"\nQuarto\n{i.getQuarto()}\n\nProdutos")
            self.displayProdutos(i.getQuarto().listaConsumo(produtos))
            print(f"\nTotal: {total}")
            print('─' * 50)
    def displayQuartos(self, quartos):
        for i in quartos:
            print(f"{i}")

    def awaitInput(self):
        print("[Aperte ENTER para continuar]")
        input()
        self.clearConsole()
    
    def printData(self, string):
        print(string)
    
    def clearConsole(self):
        os.system('cls')
    def errorMessage(self, erro, solucao):
        print("{} - {}".format(erro,solucao))
    def successMessage(self, success):
        print("{}".format(success))