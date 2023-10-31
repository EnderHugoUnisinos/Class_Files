class Veiculo():
    def __init__(self, ano = None, peso = None, tanque = None, modelo = None) -> None:
        self.ano = ano
        self.peso = int(peso)
        self.tanque = int(tanque)
        self.modelo = modelo
    
    def info(self):
        return f"Veiculo(Ano: {self.ano}, Peso: {self.peso}, Tanque: {self.tanque}, Modelo: {self.modelo})"