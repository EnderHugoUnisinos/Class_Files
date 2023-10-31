from veiculo import Veiculo

class Aquatico(Veiculo):
    def __init__(self, ano, peso, tanque, modelo, qtMotor, qtConves) -> None:
        super().__init__(ano, peso, tanque, modelo)
        self.qtMotor = int(qtMotor)
        self.qtConves = int(qtConves)

    def info(self):
        return f"Aquatico(Motores: {self.qtMotor}, Convés: {self.qtConves}, Consumo: {self.consumo()}, Autonomia: {self.autonomia()}) {super().info()}"
    
    def consumo(self):
        return 1/((self.peso * 0.00002) + (self.qtMotor *0.02))

    def autonomia(self):
        return self.tanque / self.consumo()