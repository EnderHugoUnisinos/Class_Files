class SystemController:
    def __init__(self, pousada_path, produto_path, quarto_path, reserva_path) -> None:
        self.pousada_path = pousada_path
        self.produto_path = produto_path
        self.quarto_path = quarto_path
        self.reserva_path = reserva_path

    #def controller_salvar_dados(self, pousada):
    #    with open(self.pousada_path, "w") as file:
    #        file.write()

    #def controller_carregar_dados(self, pousada):
    #    with open(self.pousada_path, "r") as file:
    #        strings = file.readlines()