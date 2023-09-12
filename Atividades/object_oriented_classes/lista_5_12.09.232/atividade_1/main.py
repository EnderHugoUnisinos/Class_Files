from pessoa import Pessoa

class System():
    def programStart(self):
        file = "objetos.csv"

        pessoa1 = Pessoa(0, "A", "F", "18", "1.70", "91")
        pessoa1.visualizar()
        pessoa1.carregar(file)
        pessoa1.salvar(file)
        
        pessoa2 = Pessoa(1, "B", "M", "19", "1.80", "84")
        pessoa2.visualizar()
        pessoa2.carregar(file)
        pessoa2.salvar(file)
        
        pessoa3 = Pessoa(2, "C", "F", "20", "1.90", "78")
        pessoa3.visualizar()
        pessoa3.carregar(file)
        pessoa3.salvar(file)

def main():
    system = System()
    system.programStart()

if __name__ == "__main__":
    main()