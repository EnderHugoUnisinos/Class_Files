class Revenda:
    def __init__(self, lista_veiculos = []):
        self.__lista_veiculos = lista_veiculos

    @property
    def lista_veiculos(self):
        return self.__lista_veiculos
    
    @lista_veiculos.setter
    def lista_veiculos(self, lista_veiculos):
        self.__lista_veiculos = lista_veiculos
    