from vip import Vip
class CamaroteInferior(Vip):
    def __init__(self) -> None:
        self.localizacao = "Camarote Inferior"
        super().__init__()
        self.valor_vip = self.valor_base + 30
    def getLocalizacao(self):
        return self.localizacao