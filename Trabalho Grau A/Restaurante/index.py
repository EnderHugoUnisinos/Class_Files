from menu import Menu
from pedidos import Pedidos
from conta import self

class index:
    while True:
        fullOrder = Menu.Order(Menu)
        Pedidos.armazenar(fullOrder, Pedidos)
        self.imprimir(Pedidos, self)
        while True:
            loop = input("Realizar outro pedido (s/n): ")
            if loop == "s":
                break
            if loop == "n":
                break
            else:
                print("Valor invalido")
                continue
        if loop == "s":
            Pedidos.limpar(Pedidos)
            continue
        else:
            input("Aperte [Enter] para sair")
            quit()