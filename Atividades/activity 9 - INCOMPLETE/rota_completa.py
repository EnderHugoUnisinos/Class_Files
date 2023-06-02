def rotaCompleta(cidades):
    listaSelCidades = []
    while True():
        tempInput = input()
        if tempInput == "fim":
            if len(listaSelCidades) >= 3:
                break
            else:
                continue
        if cidades.count(tempInput) == 0:
            print("Cidade inválida")
        elif listaSelCidades.count(tempInput) > 0:
            print("Cidade inserida multiplas vezes")
        else:
            listaSelCidades.append(tempInput)
def calcularRota():
    pass
