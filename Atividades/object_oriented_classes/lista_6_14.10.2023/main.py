from terrestre import Terrestre
from aereo import Aereo
from aquatico import Aquatico

class System():
    def __init__(self) -> None:
        self.startSystem()
    
    def startSystem(self):
        print(Terrestre(2001, 1200, 20, "Carro", 4, 4).info())
        print(Aereo(2001, 1200, 20, "Avião", 2, 2).info())
        print(Aquatico(2001, 1200, 20, "Barco", 2, 1).info())



def main():
    System()

if __name__ == "__main__":
    main()