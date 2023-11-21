from forma_bidimensional import *
from forma_tridimensional import *
class System():
    def __init__(self) -> None:
        self.formas = []
        self.menu()
        
    def menu(self):
        while True:
            print("\n[1] : Criar forma")
            print("[2] : Imprimir formas")
            print("[0] : Sair\n")
            
            user_input = input("Selecione uma das opções acima: ")
            match user_input:
                case "0":
                    quit()
                case "1":
                    self.criarForma()
                case "2":
                    self.imprimirFormas()
                case _:
                    print("Por favor escolha uma das opções presentes no menu.")
    
    def criarForma(self):
        print("\n[1] : Bidimensional")
        print("[2] : Tridimensional")
        user_input = input("A sua forma é: ")
        if (user_input == "1"):
            print("\n[1] : Circulo")
            print("[2] : Quadrado")
            print("[3] : Triangulo")
            user_input = input("A sua forma é: ")
            match user_input:
                case "1":
                    raio = input("Raio : ")
                    char = input("Caractere : ")
                    tamanho = input("Tamanho : ")
                    self.formas.append(Circulo(raio, char, tamanho))
                case "2":
                    lado = input("Lado : ")
                    char = input("Caractere : ")
                    tamanho = input("Tamanho : ")
                    self.formas.append(Quadrado(lado, char, tamanho))
                case "3":
                    lado = input("Lado : ")
                    char = input("Caractere : ")
                    tamanho = input("Tamanho : ")
                    self.formas.append(Triangulo(lado, char, tamanho))
        elif (user_input == "2"):
            print("\n[1] : Esfera")
            print("[2] : Cubo")
            print("[3] : Tetraedro")
            user_input = input("A sua forma é: ")
            match user_input:
                case "1":
                    raio = input("Raio : ")
                    self.formas.append(Esfera(raio))
                case "2":
                    aresta = input("Aresta : ")
                    self.formas.append(Cubo(aresta))
                case "3":
                    aresta = input("Aresta : ")
                    self.formas.append(Tetraedro(aresta))

    def imprimirFormas(self):
        for i in self.formas:
            print(f"\n{i}")

def main():
    System()

if __name__ == "__main__":
    main()