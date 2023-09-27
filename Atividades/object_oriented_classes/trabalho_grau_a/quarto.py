class Quarto:
    def __init__ (self, numero = None, categoria = None, diaria = None, consumo = []):
        self.numero = numero
        self.categoria = categoria
        self.diaria = diaria
        self.consumo = consumo
        
    def adiciona_consumo(self, consumo):
        self.consumo.append(consumo)

    def lista_consumo(self):
        return self.consumo

    def valor_total_consumo(self):
        pass

    def limpa_consumo(self):
        self.consumo = []

    def serializar(self):
        consumo_string = ""
        for j in self.lista_consumo():
            consumo_string = "{}{}|".format(consumo_string, j)
        consumo_string = consumo_string[:-1]
        serialized_string = "{}/{}/{}/{}".format(serialized_string,self.numero,self.categoria,self.diaria,consumo_string)
        return serialized_string
    
    def deserializar(self):
        pass