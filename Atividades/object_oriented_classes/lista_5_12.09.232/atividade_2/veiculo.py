class Veiculo:
    def __init__(self, codigo, fabricante, modelo, ano, motor, preco):
        self.codigo = codigo
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.motor = motor
        self.preco = preco
    
    def serializacao(self):
        return "{},{},{},{},{},{}".format(self.codigo,self.fabricante,self.modelo,self.ano,self.motor,self.preco)

    def deserializacao(self):
        pass