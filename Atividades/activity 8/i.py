def content(frase):
    resultado = ""
    frase = frase
    if(frase.isnumeric()):
            resultado = "Inteiro"
    frase = frase.replace(".", "").replace(",", "")
    if(frase.isalpha()):
        resultado = "Alfabetico"
    else:
        resultado = "Fracionario"
    return resultado

frase = input("Insira texto, numero inteiro ou fracionario: ")
print(content(frase))