def tabela(frase):
    strip = frase.strip().replace(" ", "").upper()
    dictionary = {}
    for i in strip:
        dictionary[i] = strip.count(i)
    return dictionary

frase = input("Digite uma palavra/frase: ")

print(tabela(frase))
