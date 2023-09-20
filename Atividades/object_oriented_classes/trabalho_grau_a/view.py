class SystemView:
    def __init__(self) -> None:
        pass

    def view_menu_principal():
        print("[1] : Consultar disponibilidade")
        print("[2] : Consultar reserva")
        print("[3] : Realizar reserva")
        print("[4] : Cancelar reserva")
        print("[5] : Realizar check-in")
        print("[6] : Realizar check-out")
        print("[7] : Registrar consumo")
        print("[8] : Quartos")
        print("[9] : Produtos")
        print("[10] : Salvar")
        print("[0] : Sair")
        user_input = input("Insira a opção desejada: ")
        return user_input

    def view_menu_quartos(self):
        print("[1] : Adicionar quarto")
        print("[2] : Remover quarto")
        print("[3] : Adicionar multiplos quartos")
        print("[4] : Remover multiplos quartos")
        print("[5] : Listar quartos")
        print("[0] : Voltar ao menu principal")
        user_input = input("Insira a opção desejada: ")
        return user_input
    
    def view_menu_produtos(self):
        print("[1] : Adicionar produto")
        print("[2] : Produto quarto")
        print("[3] : Modificar produto")
        print("[4] : Listar produtos")
        print("[0] : Voltar ao menu principal")
        user_input = input("Insira a opção desejada: ")
        return user_input