from jogador import Jogador
class System():
    def iniciar_programa(self):
        jogador_teste = Jogador("ricardo","atacante","16-10-1990","brasileiro",80)
        print(f"{jogador_teste}")
        print(f"Idade: {jogador_teste.calcular_idade()}")
        print(f"Tempo para aposentadoria: {jogador_teste.calcular_tempo_para_aposentadoria()}")
        
def main():
    system = System()
    system.iniciar_programa()

if __name__ == "__main__":
    main()