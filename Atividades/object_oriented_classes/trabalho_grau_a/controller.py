class SystemController:
    def __init__(self, path) -> None:
        self.path = path

    def controller_salvar_dados(self, pousada):
        with open(self.path, "w") as file:
            file.write()

    def controller_carregar_dados(self, pousada):
        with open(self.path, "r") as file:
            strings = file.readlines()