from pousada import Pousada
from utils import Utils
class SystemModel:
    def __init__(self, pousada_path, produto_path, quarto_path, reserva_path) -> None:
        self.pousada_path = pousada_path
        self.produto_path = produto_path
        self.quarto_path = quarto_path
        self.reserva_path = reserva_path
        self.pousada = Pousada()
    
    def get_paths(self):
        return [self.pousada_path, self.produto_path, self.quarto_path, self.reserva_path]

    def get_pousada(self):
        return self.pousada

    def salvar_dados(self):
        dadosDict = self.pousada.salvar_dados()
        paths = self.get_paths()
        self.write_to_file(dadosDict["pousada"], paths[0])
        self.write_to_file(dadosDict["produtos"], paths[1])
        self.write_to_file(dadosDict["quartos"], paths[2])
        self.write_to_file(dadosDict["reservas"], paths[3])

    def carregar_dados(self):
        paths = self.get_paths()
        pousadaString = self.read_from_file(paths[0])
        produtoStrings = self.read_from_file(paths[1])
        quartoStrings = self.read_from_file(paths[2])
        reservaStrings = self.read_from_file(paths[3])
        self.get_pousada().carregar_dados(pousadaString, quartoStrings, reservaStrings, produtoStrings)
    
    def realizar_check_in(self, reservas):
        self.get_pousada().realizar_check_in(reservas)
    
    def realizar_check_out(self, reservas):
        return self.get_pousada().realizar_check_out(reservas)

    def search_for_reservas(self, cliente):
        return self.get_pousada().search_for_reservas(cliente)

    def cancelar_reserva(self, cliente):
        self.get_pousada().cancela_reserva(cliente)

    def realizar_reserva(self, dados):
        self.get_pousada().realiza_reserva(dados["dia_inicio"],dados["dia_fim"],dados["cliente"],self.get_pousada().search_for_quarto(dados["quarto"]))

    def get_produtos(self):
        produtos = self.get_pousada().get_produtos()
        return produtos
    
    def write_to_file(self, string_list, path):
        try:
            with open(path, "w") as file:
                file.writelines(line + "\n" for line in string_list)
            return True
        except: 
            return False
    
    def read_from_file(self, path):
        try:
            with open(path, "r") as file:
                string = file.readlines()
            return string
        except:
            return False

    def consultar_disponibilidade(self, data, quarto):
        return self.get_pousada().consulta_disponibilidade(data, quarto)
        
    def consultar_reserva(self, data, cliente, quarto):
        return self.get_pousada().consulta_reserva(data, cliente, quarto)

    def registrar_consumo(self, cliente, consumo):
        modified = 0
        for i in self.search_for_reservas(cliente):
            quarto = i.get_quarto()
            for j in consumo:
                quarto.adiciona_consumo(j)
                modified += 1
        return modified