from main import SystemView
class SystemModel:
    def __init__(self) -> None:
        self.view = SystemView()

    def model_menu_principal(self):
        user_input = self.view.view_menu_principal()
        match user_input:
            case 0:
                quit()
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                self.model_menu_quartos()
            case 9:
                pass
            case default:
                pass
    
    def model_menu_quartos(self):
        user_input = self.view.view_menu_quartos()
        match user_input:
            case 0:
                self.model_menu_principal()
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case default:
                pass

    def model_menu_produtos(self):
        user_input = self.view.view_menu_produtos()
        match user_input:
            case 0:
                self.model_menu_principal()
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case default:
                pass
        
        