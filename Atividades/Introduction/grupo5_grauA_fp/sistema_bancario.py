import os
import sys

nome_cliente = ""
saldo_inicial = 0.0
saldo_atual = 0.0
quantidade_depositos = 0
valor_total_depositos = 0.0
quantidade_saques = 0
valor_total_saques = 0.0
valor_total_juros = 0.0
conta_aberta = False


def abrir_conta():
    # Brunno Calgarotto
    # código para criar uma nova conta
    global nome_cliente
    global saldo_inicial
    global saldo_atual
    global conta_aberta

    os.system('cls' if os.name == 'nt' else 'clear')
    nome_cliente = input('Digite o nome da sua conta: ')
    while True:
        try:
            saldo_inicial = float(input('Digite seu saldo inicial: '))
        except:
            print("Valor informado não é valido.")
            continue
        break
    saldo_atual = saldo_inicial
    conta_aberta = True
    print("\n")
    print('Sua conta é:', nome_cliente)
    print('Seu saldo inicial é: R${}'.format(saldo_inicial))
    input("\nAperte [Enter] para continuar\n")
    os.system('cls' if os.name == 'nt' else 'clear')

def realizar_deposito():
    #Brunno Calgarotto
    # código para realizar um depósito
    global valor_total_depositos
    global quantidade_depositos
    global saldo_atual
    global saldo_inicial

    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        try:
            deposito = float(input('Quanto você quer depositar? '))
        except:
            print("Valor informado não é valido.")
            continue
        if deposito <= 0.0:
            print("Valor deve ser maior que zero.")
            continue
        else:
            break

    quantidade_depositos += 1
    valor_total_depositos += deposito
    saldo_atual = valor_total_depositos+saldo_inicial

    print('\n')
    print('Você depositou: R${}'.format(deposito))
    print('Seu saldo atual é: R${}'.format(saldo_atual))
    input("\nAperte [Enter] para continuar\n")
    os.system('cls' if os.name == 'nt' else 'clear')

def realizar_saque():
    # Ender
    # código para realizar um saque
    global quantidade_saques 
    global valor_total_saques 
    global saldo_atual 
    
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        try:
            saque = float(input("Insira o valor a ser sacado: "))
        except:
            print("Valor informado não é valido.")
            continue
        if saque <= 0.0:
            print("Valor deve ser maior que zero.")
            continue
        elif saque > saldo_atual:
            print("Saldo insuficiente.")
            continue
        else:
            contador = 0
            notas = [0,0,0,0,0,0]
            #Teste se é possivel retirar valor nas notas disponiveis
            while True:
                if saque >= 100:
                    saque -= 100
                    contador += 100
                    notas[0] += 1
                elif saque >= 50:
                    saque -= 50
                    contador += 50
                    notas[1] += 1
                elif saque >= 20:
                    saque -= 20
                    contador += 20
                    notas[2] += 1
                elif saque >= 10:
                    saque -= 10
                    contador += 10
                    notas[3] += 1
                elif saque >= 5:
                    saque -= 5
                    contador += 5
                    notas[4] += 1
                elif saque >= 2:
                    saque -= 2
                    contador += 2
                    notas[5] += 1
                else:
                    break
            if saque > 0:
                print("Saque não pode ser realizado com sucesso.")
                continue
            else:
                print("\nSaque realizado com sucesso.")
                if notas[0] > 0:
                    print("Notas de 100 : {}".format(notas[0]))
                if notas[1] > 0:
                    print("Notas de 50  : {}".format(notas[1]))
                if notas[2] > 0:
                    print("Notas de 20  : {}".format(notas[2]))
                if notas[3] > 0:
                    print("Notas de 10  : {}".format(notas[3]))
                if notas[4] > 0:
                    print("Notas de 5   : {}".format(notas[4]))
                if notas[5] > 0:
                    print("Notas de 2   : {}".format(notas[5]))
                print("Valor sacado : {} \n".format(contador))
                break
    quantidade_saques += 1
    valor_total_saques += contador
    saldo_atual -= contador
    print("Saldo atual: {} \n".format(saldo_atual))
    input("\nAperte [Enter] para continuar\n")
    os.system('cls' if os.name == 'nt' else 'clear')

def simular_emprestimo():
    # José Henrique
    # código para simular um empréstimo
    
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        try:
            valor_emprestimo = float(input('Informe o valor que deseja solicitar empresatado ao banco: '))
        except:
            print("Valor informado não é valido.")
            continue
        if valor_emprestimo <= 0.0:
            print("Valor deve ser maior que zero.")
            continue
        else:
            break

    while True:
        try:
            meses = int(input('Informe em quantas parcelas deseja dividir seu empréstimo: '))
        except:
            print("O número de parcelas informado não é valido.")
            continue
        if meses <= 0.0:
            print("O número de parcelas deve ser maior que zero.")
            continue
        else:
            break

    juros = valor_emprestimo*0.02*meses
    parcelas = (valor_emprestimo+juros)/meses
    valor_total_emprestimo = valor_emprestimo+juros

    print('A taxa de juros sobre os empréstimos é de 2% ao mês.')
    print('\nO valor total a ser pago, considerando os juros, é: R${}'.format(valor_total_emprestimo))
    print('\nO valor mensal de cada parcela, considerando os juros sobre elas é: R${}'.format(parcelas))
    print('\nO total de juros sobre o seu empréstimo é de: R${}'.format(juros))

    input("\nAperte [Enter] para continuar\n")
    os.system('cls' if os.name == 'nt' else 'clear')

def extrato():
    # José Henrique
    # código para mostrar o extrato da conta
    global nome_cliente
    global saldo_inicial
    global saldo_atual
    global quantidade_depositos
    global valor_total_depositos
    global quantidade_saques
    global valor_total_saques
    global valor_total_juros

    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        try:
            tempo_conta = int(input('Para prosseguir, informe há quantos meses você abriu sua conta: '))
        except:
            print("A quantidade de meses informada não é valida.")
            continue
        if tempo_conta <= 0.0:
            print("A quantidade de meses deve ser maior que zero.")
            continue
        else:
            break
    
    valor_total_juros = tempo_conta*saldo_atual*0.02
    saldo_atual += valor_total_juros

    print('\nEXTRATO BANCÁRIO:')
    print('\nOlá {}'.format(nome_cliente))
    print('Saldo inicial: R${}'.format(saldo_inicial))
    print('Saldo atual: R${}'.format(saldo_atual))
    print('Depósitos realizados: {}'.format(quantidade_depositos))
    print('Valor total de depósitos realizados: R${}'.format(valor_total_depositos))
    print('Saques realizados: {}'.format(quantidade_saques))
    print('Valor total dos saques realizados: R${}'.format(valor_total_saques))
    print('Valor total de juros recebidos: R${} (com base na taxa de rendimento de 2% ao mês.)'.format(valor_total_juros))
    input("\nAperte [Enter] para continuar\n")
    os.system('cls' if os.name == 'nt' else 'clear')

def sair():
    # José Henrique
    # código para sair
    sair = input('Deseja sair? \nDigite [1] para sair ou aperte qualquer tecla para voltar ao menu. ')
    if sair ==  "1":
        sys.exit('Saindo...')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        return

def menu():
    # código para exibir o menu e chamar as funções correspondentes / Lucas Roese
    while True:
        item = 0
        if conta_aberta is True:
            print('[1] Realizar depósito')
            print('[2] Realizar saque')
            print('[3] Simular empréstimo')
            print('[4] Retirar extrato')
            print('[5] Sair')
            while item not in ['1', '2', '3', '4', '5']:
                item = input('Escolha uma opção: ')  
                if item not in ['1', '2', '3', '4', '5']:
                    print('\nOpção Desconhecida\n')
            # funções das opções
            if item == '1':  
                print('\nOpção escolhida: Realizar depósito\n')
                realizar_deposito()  
            if item == '2':  
                print('\nOpção escolhida: Realizar saque\n')
                realizar_saque()
            if item == '3':
                print('\nOpção escolhida: Simular empréstimo')
                simular_emprestimo()
            if item == '4':
                print('\nOpção escolhida: Retirar extrato')
                extrato()
            if item == '5':
                print('\nOpção escolhida: Sair')
                sair()
        else:
            print('[1] Abrir conta bancária')
            print('[2] Sair')
            while item not in ['1', '2']:
                item = input('Escolha uma opção: ')
                if item not in ['1', '2']:
                    print('\nOpção Desconhecida\n')
            # funções das opções
            if item == '1':  
                print('\nOpção escolhida: Abrir conta bancária\n')
                abrir_conta()  
            if item == '2':  
                print('\nOpção escolhida: Sair\n')
                sair()

def main():
    # Ender
    # código principal do programa
    os.system('cls' if os.name == 'nt' else 'clear')
    print("------------------------------------")
    print("Bem vindo ao sistema bancario Python")
    print("------------------------------------")
    print("\n")

    menu()
    pass

# Execução do programa
if __name__ == '__main__':
    main()