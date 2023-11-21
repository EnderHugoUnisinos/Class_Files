from vip import Vip
class CamaroteSuperior(Vip):
    def __init__(self) -> None:
        self.localizacao = "Camarote Superior"
        super().__init__()
        self.valor_superior = self.valor_base + self.valor_vip + 30
    def imprimeValorCamarote(self):
        return self.valor_superior
    def getLocalizacao(self):
        return self.localizacao