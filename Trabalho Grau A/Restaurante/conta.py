from pedidos import Pedidos
from menu import Menu

class self:
    priceOrderList = []
    
    def calcular(list):
        result = 0
        for x in list:
            result = result + x
        return result
        
    def imprimir(Pedidos, self):
        CurrentOrder = Pedidos.getOrder(Pedidos)
        for x in CurrentOrder:
            self.priceOrderList.append(Menu.menuPrices[x]) 
        result = self.calcular(self.priceOrderList)
        quantidade = [CurrentOrder.count(0), CurrentOrder.count(1), CurrentOrder.count(2)]
        if quantidade[0] > 0:
            print("{} - {} : R${}".format(quantidade[0], Menu.menuItems[0], (Menu.menuPrices[0]*quantidade[0])))
        if quantidade[1] > 0:
            print("{} - {} : R${}".format(quantidade[1], Menu.menuItems[1], (Menu.menuPrices[1]*quantidade[1])))
        if quantidade[2] > 0:
            print("{} - {} : R${}".format(quantidade[2], Menu.menuItems[2], (Menu.menuPrices[2]*quantidade[2])))
        print("Total : R${}".format(result))
        return
            
        