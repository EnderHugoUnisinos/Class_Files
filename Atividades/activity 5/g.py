x = 1.0
y = 1.0
lista = []
while x != 0:
    x = int(input("insira um numero: "))
    if x != 0:
        lista.append(x)
print("Numeros digitados: {}".format(len(lista)))
x = 0
y = 0
for i in lista:
    if i % 2 == 0:
        x += 1
    else:
        y += 1
print("Quantidade de numeros pares: {}".format(x))
print("Quantidade de numeros impares: {}".format(y))
x = 0
y = 0
for i in lista:
    x += i
y = x / len(lista)
print("Soma: {}".format(x))
print("Media aritmetica: {}".format(y))
x = lista[0]
y = x
for i in lista:
    if i > x:
        x = i
    if i < y:
        y = i
    
print("Maior numero: {}".format(x))
print("Menor numero: {}".format(y))