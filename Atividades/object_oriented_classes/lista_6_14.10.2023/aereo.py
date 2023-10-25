from veiculo import Veiculo

class Aereo(Veiculo):
    def __init__(self, ano, peso, tanque, modelo, qtAsa, qtMotor) -> None:
        super().__init__(ano, peso, tanque, modelo)
        self.qtAsa = int(qtAsa)
        self.qtMotor = int(qtMotor)

    def info(self):
        return f"Aereo(Asas: {self.qtAsa}, Motores: {self.qtMotor}, Consumo: {self.consumo()}, Autonomia: {self.autonomia()}) {super().info()}"
    
    def consumo(self):
        return 1/((self.peso * 0.00002) + (self.qtMotor * 0.02))

    def autonomia(self):
        return self.tanque / self.consumo()