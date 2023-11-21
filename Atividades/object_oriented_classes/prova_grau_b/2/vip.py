from ingresso import Ingresso
class Vip(Ingresso):
    def __init__(self) -> None:
        super().__init__()
        self.valor_vip = self.valor_base + 30
    def imprimeValorVip(self):
        return self.valor_vip