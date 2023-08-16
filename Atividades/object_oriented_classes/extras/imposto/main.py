from imposto import Imposto

def main():
    data = get_user_input()
    imposto = start_class(data)
    print_data(imposto)

def get_user_input():
    data = {"nome":"", "nascimento":"", "profissao":"", "escolaridade":"", "renda_mensal":"", "numero_dependentes":""}
    
    data["nome"] = input("Nome do contribuinte: ")
    data["nascimento"] = input("Ano de nascimento (DD-MM-AAAA): ")
    data["profissao"] = input("Profissão: ")
    data["escolaridade"] = input("Escolaridade: ")
    data["renda_mensal"] = input("Renda mensal: ")
    data["numero_dependentes"] = input("Número de dependentes: ")
    
    return data

def start_class(data):
    imposto = Imposto(data["nome"],data["nascimento"],data["profissao"],data["escolaridade"],data["renda_mensal"],data["numero_dependentes"])
    return imposto

def print_data(imposto):
    print(imposto)
    pass

if __name__ == "__main__":
    main()