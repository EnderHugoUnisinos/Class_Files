from pousada import Pousada

class Sistema():
    def iniciar_programa(self):
        pousada = Pousada("Daemon's Inn", "(51)9990-0800")
    
    def menu_principal(self):
        print("[1] : Consultar disponibilidade")
        print("[2] : Consultar reserva")
        print("[3] : Realizar reserva")
        print("[4] : Cancelar reserva")
        print("[5] : Realizar check-in")
        print("[6] : Realizar check-out")
        print("[7] : Registrar consumo")
        print("[8] : Modificar quartos")
        print("[9] : Salvar")
        print("[0] : Sair")
    
    def menu_quartos(self):
        print("[1] : Adicionar quarto")
        print("[2] : Remover quarto")
        print("[3] : Adicionar multiplos quartos")
        print("[4] : Remover multiplos quartos")
        print("[5] : Listar quartos")
        print("[0] : Voltar ao menu principal")

def main():
    system = Sistema()
    system.iniciar_programa()

if __name__ == "__main__":
    main()