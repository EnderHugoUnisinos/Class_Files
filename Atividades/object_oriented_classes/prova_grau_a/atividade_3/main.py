from data import Data
import os
class System():
    def __init__(self):
        self.datas = []
    
    def iniciar_programa(self):
        self.menu()
    
    def adicionar_data(self, data):
        self.datas.append(data)

    def get_datas(self):
        return self.datas

    def menu(self):
        while True:
            print("\n")
            print("[0]: Sair")
            print("[1]: Criar data")
            print("[2]: Listar datas")
            print("[3]: Comparar datas")
            user_input = input("Insira a opção desejada: ")
            print("\n")
            clear = lambda: os.system('cls')
            clear()
            match user_input:
                case "0":
                    self.sair()
                case "1":
                    self.criar_data()
                case "2":
                    self.listar_datas()
                case "3":
                    self.comparar_datas()
                case _:
                    print("Escolha invalida, tente novamente.")
    
    def sair(self):
        exit()
    
    def criar_data(self):
        user_input = input("Insira a data no padrão (DD/MM/AAAA): ")
        self.adicionar_data(Data(user_input))
    
    def listar_datas(self):
        for id, i in enumerate(self.get_datas()):
            print(f"{id}: {str(i)}")

    def comparar_datas(self):
        user_input = [None, None]
        user_input[0] = input("Insira o id da data corrente:")
        user_input[1] = input("Insira o id da data do parametro:")
        try:
            datas = self.get_datas()
            result = datas[int(user_input[0])].compara(datas[int(user_input[1])])
            match result:
                case -1:
                    print("A data corrente é maior")
                case 0:
                    print("As datas são iguais")
                case 1:
                    print("A data do parametro é maior")
        except:
            print("Não foi possivel encontrar o id inserido")

def main():
    system = System()
    system.iniciar_programa()

if __name__ == "__main__":
    main()