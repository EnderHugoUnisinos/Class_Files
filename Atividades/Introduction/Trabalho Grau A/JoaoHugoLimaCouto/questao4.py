numeroAtual = 1
listaNumeros = []
listaPares = []
listaImpares = []
while numeroAtual != 0:
    try:
        numeroAtual = int(input("Insira um valor inteiro: "))
        if numeroAtual != 0:
            listaNumeros.append(numeroAtual)
        if len(listaNumeros) == 0:
            print("Lista deve ter ao menos um valor!")
            numeroAtual = 1
    except:
        print("Valor invalido, digite outro valor.")
        continue

total = 0
tamanho = len(listaNumeros)

for index in listaNumeros:
    if (index%2) == 0:
        listaPares.append(index)
    else:
        listaImpares.append(index)
    total += index
    
media = total / tamanho
totalPares = 0
totalImpares = 0
if len(listaPares) != 0:
    parMenor = listaPares[0]
else:
    parMenor = 0
imparMaior = 0

for index in listaPares:
    totalPares += index
    if index < parMenor:
        parMenor = index
for index in listaImpares:
    totalImpares += index
    if index > imparMaior:
        imparMaior = index
if totalPares == 0:
    print("[Lista não possuia numeros pares]")
else:
    print("Somatório dos numeros pares   : {}".format(totalPares))
if totalImpares == 0:
    print("[Lista não possuia numeros impares]")
else:
    print("Somatório dos numeros impares : {}".format(totalImpares))
if parMenor == 0:
    print("[Lista não possuia numeros pares]")
else:
    print("Menor número par              : {}".format(parMenor))
if imparMaior == 0:
    print("[Lista não possuia numeros impares]")
else:
    print("Maior número impar            : {}".format(imparMaior))
print("Média de todos os valores     : {:.2f}".format(media))