import os
class Menu:
    menuItems = ["Hamburguer","Batata frita","Refrigerante"]
    menuPrices = [15.00, 7.00, 5.00]
    fullOrder = []

    def Order(self):
        while True:
            print("[0] Finalizar pedido")
            print("[1] {} : R${}".format(self.menuItems[0],self.menuPrices[0]))
            print("[2] {}: R${}".format(self.menuItems[1],self.menuPrices[1]))
            print("[3] {}: R${}".format(self.menuItems[2],self.menuPrices[2]))
            order = int(input("Insira o valor correspondente a opção desejada: "))
            match order:
                case 0:
                    print("Finalizando pedido")
                    break
                case 1:
                    print("Hamburguer")
                    self.fullOrder.append(0)
                case 2:
                    print("Batata frita")
                    self.fullOrder.append(1)
                case 3:
                    print("Refrigerante")
                    self.fullOrder.append(2)
                case _:
                    print("Valor inserido é invalido")
        return self.fullOrder
                    