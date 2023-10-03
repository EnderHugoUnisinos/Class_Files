from pousada import Pousada
class SystemController:
    def __init__(self, pousada_path, produto_path, quarto_path, reserva_path) -> None:
        self.pousada_path = pousada_path
        self.produto_path = produto_path
        self.quarto_path = quarto_path
        self.reserva_path = reserva_path
        self.pousada = Pousada()
    
    def salvar_dados(self):
        dadosDict = self.pousada.salvarDados()
        self.write_to_file(dadosDict["pousada"], self.pousada_path)
        self.write_to_file(dadosDict["produtos"], self.produto_path)
        self.write_to_file(dadosDict["quartos"], self.quarto_path)
        self.write_to_file(dadosDict["reservas"], self.reserva_path)

    def carregar_dados(self):
        pousadaString = self.read_from_file(self.pousada_path)
        quartoStrings = self.read_from_file(self.quarto_path)
        reservaStrings = self.read_from_file(self.reserva_path)
        produtoStrings = self.read_from_file(self.produto_path)
        self.pousada.carregarDados(pousadaString, quartoStrings, reservaStrings, produtoStrings)
    
    def cancelar_reserva(self, cliente):
        self.pousada.cancelaReserva(cliente)

    def realizar_reserva(self, dados):
        self.pousada.realizaReserva(dados["dia_inicio"],dados["dia_fim"],dados["cliente"],self.pousada.searchQuarto(dados["quarto"]))

    def get_produtos(self):
        produtos = self.pousada.produtos
        return produtos
    
    def write_to_file(self, string_list, path):
        try:
            with open(path, "w") as file:
                file.writelines(string_list)
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
        return self.pousada.consultaDisponibilidade(data, quarto)
        
    def consultar_reserva(self, data, cliente, quarto):
        return self.pousada.consultaReserva(data, cliente, quarto)


