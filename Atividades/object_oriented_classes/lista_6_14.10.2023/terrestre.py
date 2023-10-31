from veiculo import Veiculo

class Terrestre(Veiculo):
    def __init__(self, ano, peso, tanque, modelo, qtRoda, qtPorta) -> None:
        super().__init__(ano, peso, tanque, modelo)
        self.qtRoda = int(qtRoda)
        self.qtPorta = int(qtPorta)

    def info(self):
        return f"Terrestre(Rodas: {self.qtRoda}, Portas: {self.qtPorta}, Consumo: {self.consumo()}, Autonomia: {self.autonomia()}) {super().info()}"
    
    def consumo(self):
        return 1/((self.peso * 0.00005) + (self.qtRoda * 0.005))

    def autonomia(self):
        return self.tanque / self.consumo()