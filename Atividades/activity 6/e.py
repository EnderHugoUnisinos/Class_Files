ganhoPorHora = 0
horasTrabalhadas = 0
salarioBruto = 0
inss = 0
sindicato = 0
salarioLiquido = 0

def GanhoPorHora():
    while True:
        try:
            ganhoPorHora = float(input("Insira o quanto recebe por hora: "))
        except:
            print("Valor informado é invalido")
            continue
        break
    return ganhoPorHora

def HorasTrabalhadas(): 
    while True:
        try:
            horasTrabalhadas = float(input("Insira o numero de horas trabalhadas: "))
        except:
            print("Valor informado é invalido")
            continue
        break
    return horasTrabalhadas

def SalarioBruto(ganhoPorHora, horasTrabalhadas):
    salarioBruto = ganhoPorHora * horasTrabalhadas
    if(salarioBruto == 0):
        print("Não há informações suficientes para determinar valor")
        Menu()
    return salarioBruto

def INSS(salarioBruto):
    inss = salarioBruto * 0.11
    if(salarioBruto == 0):
        print("Não há informações suficientes para determinar valor")
        Menu()
    return inss

def Sindicato(salarioBruto):
    sindicato = salarioBruto * 0.02
    if(salarioBruto == 0):
        print("Não há informações suficientes para determinar valor")
        Menu()
    return sindicato

def SalarioLiquido(salarioBruto, inss, sindicato):
    salarioLiquido = salarioBruto - inss - sindicato
    if(salarioBruto == 0) or (inss == 0) or (sindicato == 0):
        print("Não há informações suficientes para determinar valor")
        Menu()
    return salarioLiquido

def Sair():    
    quit()

def Menu():
    while True:
        print("[1] - Ganho por hora")
        print("[2] - Horas trabalhadas")
        print("[3] - Salario bruto")
        print("[4] - Pago ao INSS")
        print("[5] - Pago ao sindicato")
        print("[6] - Salario liquido")
        print("[7] - Sair")
        try:
            optionChosen = int(input("Insira o numero correspondente a opção desejada: "))
        except:
            print("Valor informado não é valido")
        match optionChosen:
            case 1:
                ganhoPorHora = GanhoPorHora()
                print("Ganho por hora: {}".format(ganhoPorHora))
                input("Aperte [Enter] para continuar")
                continue
            case 2:
                horasTrabalhadas = HorasTrabalhadas()
                print("Horas trabalhadas: {}".format(horasTrabalhadas))
                input("Aperte [Enter] para continuar")
                continue
            case 3:
                salarioBruto = SalarioBruto(ganhoPorHora, horasTrabalhadas)
                print("Salario bruto: {}".format(salarioBruto))
                input("Aperte [Enter] para continuar")
                continue
            case 4:
                salarioBruto = SalarioBruto(ganhoPorHora, horasTrabalhadas)
                inss = INSS(salarioBruto)
                print("Pago ao INSS: {}".format(inss))
                input("Aperte [Enter] para continuar")
                continue
            case 5:
                salarioBruto = SalarioBruto(ganhoPorHora, horasTrabalhadas)
                sindicato = Sindicato(salarioBruto)
                print("Pago ao sindicato: {}".format(sindicato))  
                input("Aperte [Enter] para continuar")
                continue
            case 6:
                salarioBruto = SalarioBruto(ganhoPorHora, horasTrabalhadas)
                inss = INSS(salarioBruto)
                sindicato = Sindicato(salarioBruto)
                salarioLiquido = SalarioLiquido(salarioBruto, inss, sindicato)
                print("Salario liquido: {}".format(salarioLiquido))
                input("Aperte [Enter] para continuar")
                continue
            case 7:
                Sair()
            case _:
                print("Valor informado invalido")
                continue
Menu()