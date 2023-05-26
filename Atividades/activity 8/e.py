def Palindromo(frase):
    frase = frase.lower()
    semEspaco = frase.strip().replace(" ", "")
    invert = semEspaco[::-1]
    if (semEspaco == invert):
        palindromo = True
    else:
        palindromo = False
    return palindromo

frase = input("Digite uma palavra/frase: ")
resultado = Palindromo(frase)
print(resultado)