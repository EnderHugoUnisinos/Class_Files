from elevador import Elevador
class System():
    def iniciar_programa(self):
        elevador_teste = Elevador(5,6)
        elevador_teste.entrar()
        elevador_teste.subir()
        elevador_teste.sair()
        elevador_teste.descer()
        print(elevador_teste)
        
def main():
    system = System()
    system.iniciar_programa()

if __name__ == "__main__":
    main()