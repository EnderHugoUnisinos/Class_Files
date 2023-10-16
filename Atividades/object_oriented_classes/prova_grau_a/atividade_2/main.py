from elevador import Elevador
class System():
    def __init__(self):
        self.elevador = Elevador(10, 6)

    def iniciar_programa(self):
        self.menu()

    def menu(self):
        while True:
            print("_"*50)
            print(f"Andar: {self.elevador.get_andar_atual()}, Pessoas presentes: {self.elevador.get_pessoas_presentes()}\n")
            print("[1]: Entrar no elevador")
            print("[2]: Sair do elevador")
            print("[3]: Subir um andar")
            print("[4]: Descer um andar")
            print("[5]: Ver status do elevador")
            print("[6]: Inicializar")
            print("[0]: Sair")

            user_input = input("Entre sua escolha: ")
            print("\n")

            match user_input:
                case '1':
                    if not self.elevador.entrar():
                        print("Limite atingido, não foi possivel entrar.")
                case '2':
                    if not self.elevador.sair():
                        print("Elevador vazio, não foi possivel sair.")
                case '3':
                    if not self.elevador.subir():
                        print("Ultimo andar atingido, não é possivel subir.")
                case '4':
                    if not self.elevador.descer():
                        print("Terreo atingido, não é possivel descer")
                case '5':
                    print(self.elevador)
                case '6':
                    self.inicializar_elevador()
                case '0':
                    quit()
                case _:
                    print("Escolha invalida, tente novamente.")

    def inicializar_elevador(self):
        total_andares = int(input("Insira o numero de andares: "))
        capacidade = int(input("Insira a capacidade maxima: "))
        self.elevador.inicializar(total_andares, capacidade)

def main():
    system = System()
    system.iniciar_programa()

if __name__ == "__main__":
    main()