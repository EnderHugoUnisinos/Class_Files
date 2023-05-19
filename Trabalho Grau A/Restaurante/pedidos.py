class Pedidos:
    def armazenar(fullOrder, self):
        self.CurrentOrder = fullOrder
    def getOrder(self):
        return self.CurrentOrder
    def limpar(self):
        self.CurrentOrder.clear()