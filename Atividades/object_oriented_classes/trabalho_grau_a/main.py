from controller import SystemController
class System():
    def iniciar_programa(self):
        #could be just SystemController().menu_principal()
        system_controller = SystemController()
        system_controller.menu_principal()

def main():
    system = System()
    system.iniciar_programa()

if __name__ == "__main__":
    main()