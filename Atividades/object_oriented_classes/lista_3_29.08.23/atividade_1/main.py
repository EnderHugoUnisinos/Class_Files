from pessoa import Pessoa

class System():
    def startPerson(self):
        mae = Pessoa("Mae", "F", "A")
        mae.imprimeDados()
        
        pai = Pessoa("Pai", "M", "A")
        pai.imprimeDados()
        
        filho = mae.geraPessoa("Filho","M",pai)
        filho.imprimeDados()

def main():
    system = System()
    system.startPerson()

if __name__ == "__main__":
    main()