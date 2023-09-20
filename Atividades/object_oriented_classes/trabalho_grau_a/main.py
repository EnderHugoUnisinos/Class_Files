from model import SystemModel
class System():
    def iniciar_programa(self):
        system_model = SystemModel()
        system_model.model_menu_principal()

def main():
    system = System()
    system.iniciar_programa()

if __name__ == "__main__":
    main()