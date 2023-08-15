cidade = "null"

def validarDDD(ddd):
    match ddd:
        case "61":
            cidade = "Brasília"
        case "71":
            cidade = "Salvador"
        case "11":
            cidade = "São Paulo"
        case "21":
            cidade = "Rio de Janeiro"
        case _:
            cidade = "null"
            print("DDD não cadastrado")
    return cidade

while cidade == "null":
    ddd = input("Insira código de DDD: ")
    cidade = validarDDD(ddd)
print("\nDDD : {} | Cidade : {}".format(ddd, cidade))