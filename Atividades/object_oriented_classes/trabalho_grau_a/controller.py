from view import SystemView
from model import SystemModel   
from utils import Utils

class SystemController:
    def __init__(self) -> None:
        self.view = SystemView()
        self.model = SystemModel("assets/pousada.txt","assets/produto.txt","assets/quarto.txt","assets/reserva.txt")
        self.model.carregar_dados()

    def menu_principal(self):
        while True:
            user_input = self.view.menu_principal()
            match user_input:
                case "0":
                    quit()
                case "1":
                    self.consultar_disponibilidade()
                case "2":
                    self.consultar_reserva()
                case "3":
                    self.realizar_reserva()          
                case "4":
                    self.cancelar_reserva()
                case "5":
                    self.realizar_check_in()
                case "6":
                    self.realizar_check_out()
                case "7":
                    self.registrar_consumo()
                case "8":
                    self.menu_quartos()
                case "9":
                    self.menu_produtos()
                case "10":
                    self.model.salvar_dados()
                case default:
                    self.view.error_message("Numero inserido invalido","Insira um numero presente no menu (0 - 9)")
            self.view.await_input()
        
    def consultar_disponibilidade(self):
        user_input = self.view.consultar_disponibilidade()
        result = self.model.consultar_disponibilidade(user_input["data"], user_input["quarto"])
        self.view.clear_console()
        #Testa se a consulta retornou algo
        if result != None:
            self.view.print_data(str(result))
        else:
            self.view.print_data("Quarto indisponivel.")
    def consultar_reserva(self):
        produtos = self.model.get_produtos()
        user_input = self.view.consultar_reserva()
        result = self.model.consultar_reserva(user_input["data"],user_input["cliente"],user_input["quarto"])
        self.view.clear_console()
        if result != None:
            self.view.display_reservas(result, produtos)
        else:
            self.view.error_message("Reserva não encontrada.","Verifique se os dados inseridos estão corretos")
    def realizar_reserva(self):
        user_input = self.view.realizar_reserva()
        result = self.model.consultar_disponibilidade([user_input["dia_inicio"],user_input["dia_fim"]], user_input["quarto"])
        self.view.clear_console()
        #Testa se a consulta retornou algo
        if result == None:
            try:
                self.model.realizar_reserva(user_input)
                self.view.success_message("Reserva realizada com sucesso")
            except:
                self.view.error_message("Ocorreu um erro ao inserir a reserva","Entre em contato com o desenvolvedor")
        else:
            self.view.print_data("Quarto indisponivel.")     
    def cancelar_reserva(self):
        user_input = self.view.cancelar_reserva()
        result = self.model.consultar_reserva(None, user_input, None)
        self.view.clear_console()
        #Testa se a consulta retornou algo
        if result[0] != None:
            try:
                self.model.cancelar_reserva(user_input)
                self.view.success_message("Reserva cancelada com sucesso")
            except:
                self.view.error_message("Ocorreu um erro ao cancelar a reserva","Entre em contato com o desenvolvedor")
        else:
            self.view.print_data("Nenhuma reserva encontrada.")  
    def realizar_check_in(self):
        produtos = self.model.get_produtos()
        user_input = self.view.realizar_checkin()
        result = self.model.search_for_reservas(user_input)
        self.view.clear_console()
        if result != None:
            self.view.display_reservas(result, produtos)
            self.model.realizar_check_in(result)
        else: 
            self.view.error_message("Reserva não encontrada.","Verifique se os dados inseridos estão corretos")
    def realizar_check_out(self):
        produtos = self.model.get_produtos()
        user_input = self.view.realizar_checkout()
        result = self.model.search_for_reservas(user_input)
        self.view.clear_console()
        if result != None:
            self.view.display_reservas(result, produtos)
            self.model.realizar_check_out(result)
        else:
            self.view.error_message("Reserva não encontrada.","Verifique se os dados inseridos estão corretos")
    def registrar_consumo(self):
        produtos = self.model.get_produtos()
        user_input = self.view.registrar_consumo(produtos)
        self.model.registrar_consumo(user_input["cliente"],user_input["consumo"])

    def menu_quartos(self):
        while True:
            user_input = self.view.menu_quartos()
            match user_input:
                case "0":
                    break
                case "1":
                    self.adicionar_quarto()
                case "2":
                    self.remover_quarto()
                case "3":
                    self.adicionar_multiplos_quartos()
                case "4":
                    self.remover_multiplos_quartos()
                case "5":
                    self.listar_produtos()
                case default:
                    self.view.error_message("Numero inserido invalido","Insira um numero presente no menu (0 - 5)")
            self.view.await_input()

    def adicionar_quarto(self):
        pass
    def remover_quarto(self):
        pass
    def adicionar_multiplos_quartos(self):
        pass
    def remover_multiplos_quartos(self):
        pass
    def listar_quartos(self):
        pass

    def menu_produtos(self):
        while True:
            user_input = self.view.menu_produtos()
            match user_input:
                case "0":
                    break
                case "1":
                    self.adicionar_produto()
                case "2":
                    self.remover_produto()
                case "3":
                    self.modificar_produto()
                case "4":
                    self.listar_produtos()
                case default:
                    self.view.error_message("Numero inserido invalido","Insira um numero presente no menu (0 - 4)")
            self.view.await_input()
        
    def adicionar_produto(self):
        pass
    def remover_produto(self):
        pass
    def modificar_produto(self):
        pass
    def listar_produtos(self):
        pass