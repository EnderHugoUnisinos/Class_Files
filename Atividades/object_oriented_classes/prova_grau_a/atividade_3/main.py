from data import Data
class System():
    def __init__(self):
        self.datas = []
    
    def iniciar_programa(self):
        self.menu()
    
    def menu(self):
        #montar sistema
        print("[0]: ")
        print("[1]: ")
        print("[2]: ")
        print("[3]: ")
        
def main():
    system = System()
    system.iniciar_programa()

if __name__ == "__main__":
    main()