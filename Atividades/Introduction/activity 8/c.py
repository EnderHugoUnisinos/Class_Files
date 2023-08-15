sujeito = input("Insira o sujeito: ")
verbo = input("Insira o verbo: ")
predicado = input("Insira o predicado: ")
fraseA = f"{sujeito} {verbo} {predicado}"
fraseB = sujeito + " " + verbo + " " + predicado
fraseC = "{} {} {}".format(sujeito, verbo, predicado)
print(fraseA)
print(fraseB)
print(fraseC)