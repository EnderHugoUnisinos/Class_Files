def espaco(frase):
    strip = frase.strip().split()
    resultado = ""
    for i in strip:
        resultado = resultado + i + " "
    return resultado

frase = input("Digite uma palavra/frase: ")

print(espaco(frase))
