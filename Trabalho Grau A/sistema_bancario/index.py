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
    #
    # código para criar uma nova conta
    pass

def realizar_deposito():
    #
    # código para realizar um depósito
    pass



def realizar_saque():
    # Ender
    # código para realizar um saque
    global quantidade_saques 
    global valor_total_saques 
    global saldo_atual 
    
    while True:
        saque = float(input("Inserir valor a ser sacado: "))
        if saque <= 0.0:
            print("Valor deve ser maior que zero")
            continue
        elif saque > saldo_atual:
            print("Saldo insuficiente")
            continue
        else:
            contador = 0
            while True:
                if saque >= 100:
                    saque -= 100
                    contador += 100
                elif saque >= 50:
                    saque -= 50
                    contador += 50
                elif saque >= 20:
                    saque -= 20
                    contador += 20
                elif saque >= 10:
                    saque -= 10
                    contador += 10
                elif saque >= 5:
                    saque -= 5
                    contador += 5
                elif saque >= 2:
                    saque -= 2
                    contador += 2
                else:
                    break
            if saque > 0:
                print("Saque não pode ser realizado com sucesso")
                continue
            else:
                print("Saque realizado com sucesso")
                break
    quantidade_saques += 1
    valor_total_saques += saque
    saldo_atual -= saque

def simular_emprestimo():
    #
    # código para simular um empréstimo
    pass


def extrato():

    # código para mostrar o extrato da conta
    print('\nEXTRATO BANCÁRIO: \n')

    print('\nOlá ', nome_cliente)
    print('\nSeu saldo inicial é de: ', saldo_inicial)
    print('\nSeu saldo atual é de: ', saldo_atual)
    print('\nA quantidade de depósitos realizados é: ', quantidade_depositos)
    print('\nO valor total de depósitos realizados é ', valor_total_depositos)
    print('\nA quantidade de saques realizados é: ',quantidade_saques)
    print('\nO valor total dos saques realizados é: ', valor_total_saques)
    print('\nO valor total de juros recebios é: ', valor_total_juros)

    def sair():

        # código para encerrar o programa

        pass

    import sys

    sair = input('Deseja sair? digite "S" para sim ou "N" para não: ')

    if sair ==  "S":
        sys.exit('saindo...')
    
    else:
        menu()


def sair():
    #
    # código para encerrar o programa
    pass

def menu():
    # 
    # código para exibir o menu e chamar as funções correspondentes
    pass

def main():
    # Ender
    # código principal do programa
    print("------------------------------------")
    print("Bem vindo ao sistema bancario Python")
    print("------------------------------------")
    print("\n\n\n")

    menu()
    pass

# Execução do programa
if __name__ == '__main__':
    main()