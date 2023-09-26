class Quarto:
    def __init__ (self, id, numero, categoria, diaria, consumo = []):
        self.id = id
        self.numero = numero
        self.categoria = categoria
        self.diaria = diaria
        self.consumo = consumo

    def adicionaConsumo(self, consumo):
        self.consumo.append(consumo)

    def listaConsumo(self):
        return self.consumo

    def valorTotalConsumo(self):
        pass

    def limpaConsumo(self):
        self.consumo = []

    def serializar(self):
        pass

    def deserializar(self):
        pass