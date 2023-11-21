from normal import *
from camaroteinferior import *
from camarotesuperior import *

class Teste():
    def __init__(self) -> None:
        self.main()
        self.ingresso = None
        
    def main(self):
        while True:
            print("\n[1] : Normal")
            print("[2] : VIP")
            
            user_input = input("Selecione uma das opções acima: ")
            match user_input:
                case "1":
                    self.ingresso = Normal()
                    print(f"Ingresso normal: {self.ingresso.imprimeValor()}")
                case "2":
                    print("\n[1] : Camarote inferior")
                    print("[2] : Camarote superior")
                    
                    user_input = input("Selecione uma das opções acima: ")
                    
                    match user_input:
                        case "1":
                            self.ingresso = CamaroteInferior()
                            print(f"Ingresso VIP: {self.ingresso.getLocalizacao()} {self.ingresso.imprimeValorVip()}")
                        case "2":
                            self.ingresso = CamaroteSuperior()
                            print(f"Ingresso VIP: {self.ingresso.getLocalizacao()} {self.ingresso.imprimeValorCamarote()}")
                        case _:
                            print("Por favor escolha uma das opções presentes.")
                case _:
                    print("Por favor escolha uma das opções presentes.")

if __name__ == "__main__":
    Teste()