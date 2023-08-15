frase = input("Digite uma frase: ")
maiuscula = frase.upper()
minuscula = frase.lower()
print(maiuscula)
print(minuscula)
palavras = maiuscula.split()
primLetra = ""
for i in range(len(palavras)):
    primLetra = primLetra + palavras[i][0]
print(primLetra)