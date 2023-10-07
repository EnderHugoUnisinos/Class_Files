from utils import Utils
import os
class SystemView:
    def __init__(self) -> None:
        pass

    def menu_principal(self):
        print("[1] : Consultar disponibilidade")
        print("[2] : Consultar reserva")
        print("[3] : Realizar reserva")
        print("[4] : Cancelar reserva")
        print("[5] : Realizar check-in")
        print("[6] : Realizar check-out")
        print("[7] : Registrar consumo")
        print("[8] : Quartos")
        print("[9] : Produtos")
        print("[10] : Salvar")
        print("[0] : Sair")
        user_input = input("Insira a opção desejada: ")
        return user_input
    def consultar_disponibilidade(self):
        user_input = {"data":"","quarto":""}
        
        while True:
            quarto_prevalid = input("Insira o numero do quarto que deseja consultar: ")
            if not Utils().is_valid_room_number(quarto_prevalid):
                self.error_message("Formato de numero incorreto", "Insira um numero de quarto seguindo o padrão: 101, 102, 201...")
            else:
                break
        user_input["quarto"] = quarto_prevalid
        
        while True:
            data_prevalid = input("Insira a data no padrão DD-MM-AAAA: ")
            if not Utils().is_valid_date_format(data_prevalid):
                self.error_message("Formato de data incorreto", "Insira uma data seguindo o padrão: DD-MM-AAAA")
            else:
                break
        user_input["data"] = data_prevalid
        
        return user_input
    def consultar_reserva(self):
        user_input = {"cliente":"","data":"","quarto":""}
        
        print("Para cada campo insira os parametros pedidos ou insira \"X\" para não utilizar o parametro")
        self.await_input()
        
        cliente_prevalid = input("Insira o nome do cliente da reserva que deseja consultar: ")
        if cliente_prevalid.upper() == "X" or cliente_prevalid.strip() == "":
            user_input["cliente"] = None
        else:
            user_input["cliente"] = cliente_prevalid
        
        while True:
            quarto_prevalid = input("Insira o numero do quarto da reserva que deseja consultar: ")
            if not Utils().is_valid_room_number(quarto_prevalid) and quarto_prevalid.upper() != "X" and cliente_prevalid.strip() != "":
                self.error_message("Formato de numero incorreto", "Insira um numero de quarto seguindo o padrão: 101, 102, 201...")
            else:
                break
        if quarto_prevalid.upper() == "X" or quarto_prevalid.strip() == "":
            user_input["quarto"] = None
        else:
            user_input["quarto"] = quarto_prevalid
        
        while True:
            data_prevalid = input("Insira a data da reserva que deseja consultar no padrão DD-MM-AAAA: ")
            if not Utils().is_valid_date_format(data_prevalid) and data_prevalid.upper() != "X" and data_prevalid.strip() != "":
                self.error_message("Formato de data incorreto", "Insira uma data seguindo o padrão: DD-MM-AAAA")
            else:
                break
        if data_prevalid.upper() == "X" or data_prevalid.strip() == "":
            user_input["data"] = None
        else:
            user_input["data"] = data_prevalid
        
        return user_input
    def realizar_reserva(self):
        user_input = {"dia_inicio":"", "dia_fim":"","cliente":"","quarto":""}
        user_input["cliente"] = input("Insira o nome do cliente: ")
        
        while True:
            quarto_prevalid = input("Insira o numero do quarto: ")
            if not Utils().is_valid_room_number(quarto_prevalid):
                self.error_message("Formato de numero incorreto", "Insira um numero de quarto seguindo o padrão: 101, 102, 201...")
            else:
                break
        user_input["quarto"] = quarto_prevalid
        
        while True:
            data_prevalid = input("Insira o dia de inicio no padrão DD-MM-AAAA: ")
            if not Utils().is_valid_date_format(data_prevalid):
                self.error_message("Formato de data incorreto", "Insira uma data seguindo o padrão: DD-MM-AAAA")
            else:
                break
        user_input["dia_inicio"] = data_prevalid
        
        while True:
            data_prevalid = input("Insira o dia de inicio no padrão DD-MM-AAAA: ")
            if not Utils().is_valid_date_format(data_prevalid):
                self.error_message("Formato de data incorreto", "Insira uma data seguindo o padrão: DD-MM-AAAA")
            else:
                break
        user_input["dia_fim"] = data_prevalid
        
        return user_input
    def cancelar_reserva(self):
        user_input = input("Insira o nome do cliente da reserva que deseja cancelar: ")
        return user_input
    def realizar_checkin(self):
        user_input = input("Insira o nome do cliente da reserva que deseja realizar check-in: ")
        return user_input 
    def realizar_checkout(self):
        user_input = input("Insira o nome do cliente da reserva que deseja realizar check-out: ")
        return user_input 
    def registrar_consumo(self, produtos):
        user_input = {"cliente":"","consumo":[]}
        
        user_input["cliente"] = input("Insira o nome do cliente cujo consumo deseja reservar: ")
        
        self.display_produtos(produtos)
        raw_input = ""
        while raw_input != "X":
            raw_input = input("Insira o codigo dos produtos a registrar (um de cada vez), digite \"X\" para encerrar o registro:")
            if raw_input != "X" and Utils().is_valid_product_code(raw_input) and raw_input.strip() != "":
                user_input["consumo"].append(raw_input)
        return user_input
    
    def menu_quartos(self):
        print("[1] : Adicionar quarto")
        print("[2] : Remover quarto")
        print("[3] : Adicionar multiplos quartos")
        print("[4] : Remover multiplos quartos")
        print("[5] : Listar quartos")
        print("[0] : Voltar ao menu principal")
        user_input = input("Insira a opção desejada: ")
        return user_input
    def adicionar_quarto(self):
        user_input = {"numero":"","categoria":"","diaria":""}
        raw_input = ""
        while not Utils().is_valid_room_number(raw_input):
            raw_input = input("Insira o numero do quarto:")
        user_input["numero"] = raw_input
        while not Utils().is_valid_category(raw_input):
            raw_input = input("Insira a categoria do quarto:")
        user_input["categoria"] = raw_input
        while not Utils().is_valid_price(raw_input):
            raw_input = input("Insira a diaria do quarto:")
        user_input["diaria"] = raw_input

        return user_input
    def remover_quarto(self):
        while not Utils().is_valid_room_number(raw_input):
            raw_input = input("Insira o numero do quarto que deseja remover:")
        user_input = raw_input
        return user_input
    def adicionar_multiplos_quartos(self):
        raw_input = ""
        print("Insira os dados no padrão seguinte: numero/categoria/diaria")
        print("Ex: \"101/S/80\"")
        self.await_input()
        user_input = []
        while raw_input.upper() != "X" and raw_input.strip() != "":
            raw_input = input("Insira os dados do quarto, insira X para encerrar: ")
            try:
                numero, categoria, diaria = raw_input.split("/")
                if Utils().is_valid_room_number(numero) and Utils().is_valid_category(categoria) and Utils.is_valid_price(diaria):
                    user_input.append(raw_input)
                else:
                    self.error_message("Dados não puderam ser validados","Siga o padrão numero/categoria/diaria")
            except:
                self.error_message("Dados separados incorretamente", "Siga o padrão numero/categoria/diaria")
        return user_input
    def remover_multiplos_quartos(self):
        raw_input = ""
        user_input = []
        while raw_input.upper() != "X" and raw_input.strip() != "":
            raw_input = input("Insira o numero do quarto, insira X para encerrar: ")
            if Utils().is_valid_room_number(raw_input):
                user_input.append(int(raw_input))
            else:
                self.error_message("Não foi possivel validar o numero do quarto","Verifique o valor inserido")
        return user_input

    def menu_produtos(self):
        print("[1] : Adicionar produto")
        print("[2] : Produto quarto")
        print("[3] : Modificar produto")
        print("[4] : Listar produtos")
        print("[0] : Voltar ao menu principal")
        user_input = input("Insira a opção desejada: ")
        return user_input
    def adicionar_produto(self):
        pass
    def remover_produto(self):
        pass
    def modificar_produto(self):
        pass
    def listar_produtos(self):
        pass
    
    def display_produtos(self, produtos):
        for i in produtos:
            print(f"{i}")
            print('─' * 50)
    def display_reservas(self, reservas, produtos):
        for i in reservas:
            total = i.calcular_diaria()
            for j in i.get_quarto().lista_consumo(produtos):
                total += j.get_preco()
            print(f"\nReserva\n{i}")
            print(f"\nQuarto\n{i.get_quarto()}\n\nProdutos")
            self.display_produtos(i.get_quarto().lista_consumo(produtos))
            print(f"\nTotal: {total}")
            print('─' * 50)
    def display_quartos(self, quartos):
        for i in quartos:
            print(f"{i}")

    def await_input(self):
        print("[Aperte ENTER para continuar]")
        input()
        self.clear_console()
    
    def print_data(self, string):
        print(string)
    
    def clear_console(self):
        os.system('cls')
    def error_message(self, erro, solucao):
        print("{} - {}".format(erro,solucao))
    def success_message(self, success):
        print("{}".format(success))