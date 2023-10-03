class Quarto:
    def __init__ (self, numero = None, categoria = None, diaria = None, consumo = []):
        self.numero = numero
        self.categoria = categoria
        self.diaria = diaria
        
        #consumo provavelmente se encaixa melhor em reserva, mas vamos manter aqui de acordo com o diagrama
        self.consumo = consumo
    
    def __str__(self):
        return f'Numero: {self.numero}\nCategoria: {self.categoria}\nDiaria: {self.diaria}' 
    
    def __repr__(self):
        return f'Quarto({self.numero},{self.categoria},{self.diaria},{self.consumo})'
    
    def adiciona_consumo(self, consumo):
        self.consumo.append(consumo)

    def lista_consumo(self):
        return self.consumo

    def valor_total_consumo(self, produtos):
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
    
    def deserializar(self, string):
        split_string = string.strip().split("/")
        split_string[0] #numero
        split_string[1] #categoria
        split_string[2] #diaria
        split_string[3] #consumo
        
        self.numero = split_string[0]
        self.categoria = split_string[1]
        self.diaria = float(split_string[2])
        consumoString = split_string[3]
        self.consumo = consumoString.strip().split(":")
        return self