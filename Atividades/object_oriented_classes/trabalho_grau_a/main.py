from controller import SystemController
class System():
    def iniciarPrograma(self):
        #could be just SystemController().menuPrincipal()
        systemController = SystemController()
        systemController.menuPrincipal()

def main():
    system = System()
    system.iniciarPrograma()

if __name__ == "__main__":
    main()