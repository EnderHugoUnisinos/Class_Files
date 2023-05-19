def listagem (num1, num2):
    lista = []
    if num1 < num2:
        for index in range(num1+1, num2, 1):
            lista.append(index)
    elif num1 > num2:
        for index in range(num1-1, num2, -1):
            lista.append(index)
    else:
        lista = "vazia"
    return lista
            

while True:
    try:
        num1 = int(input("Insira o primeiro valor: "))
        num2 = int(input("Insira o segundo valor: "))
        break
    except:
        print("Valor informado não é valido")
        continue
lista = listagem(num1, num2)
if lista != "vazia":
    print("Lista de valores: ")
    print("{} -> {} -> {}".format(num1, lista, num2))
else:
    print("Valores iguais")