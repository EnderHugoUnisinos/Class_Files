from pais import Pais
from continente import Continente

class System():
    def iniciarPais(self):
        pais1 = Pais("A", "A", 10, 50)
        pais2 = Pais("B", "B", 20, 30)
        pais3 = Pais("C", "C", 30, 20)
        pais4 = Pais("D", "D", 40, 70)

        pais1.inserirFronteira([pais2,pais3,pais4])
        pais2.inserirFronteira([pais1,pais3,pais4])

        continente = Continente("Polvo", [pais1,pais2,pais3,pais4])
        print("Densidade total: {}".format(continente.densidadeTotal()))
        print("Dimensão total: {}".format(continente.dimensaoTotal()))
        print("Razão territorial: {}".format(continente.razaoTerritorial()))
        

def main():
    system = System()
    system.iniciarPais()

if __name__ == "__main__":
    main()