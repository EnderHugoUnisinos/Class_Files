class Quarto:
    def __init__ (self, numero = None, categoria = None, diaria = None, consumo = []):
        self.numero = numero
        self.categoria = categoria
        self.diaria = diaria
        
        #consumo provavelmente se encaixa melhor em reserva, mas vamos manter aqui de acordo com o diagrama
        self.consumo = consumo
    
    def __str__(self):
        return f'Numero: {self.get_numero()}, Categoria: {self.get_categoria()}, Diaria: {self.get_diaria()}'     
    def __repr__(self):
        return f'Quarto({self.get_numero()},{self.get_categoria()},{self.get_diaria()},{self.get_consumo()})'
    
    def get_numero(self):
        return self.numero
    def get_categoria(self):
        return self.categoria
    def get_diaria(self):
        return self.diaria
    def get_consumo(self):
        return self.consumo
    
    def set_numero(self, numero):
        self.numero = numero
    def set_categoria(self, categoria):
        self.categoria = categoria
    def set_diaria(self, diaria):
        self.diaria = diaria
    def set_consumo(self, consumo):
        self.consumo = consumo

    def adiciona_consumo(self, codigo):
        self.consumo.append(codigo)

    def lista_consumo(self, produtos):
        lista_consumo = []
        for i in self.get_consumo():
            for j in produtos:
                if j.get_codigo() == i:
                    lista_consumo.append(j)
        return lista_consumo
    
    def valor_total_consumo(self, produtos):
        total_value = 0
        for i in self.get_consumo():
            for j in produtos:
                if j.get_codigo() == i:
                    total_value += j.get_preco()
        
        return total_value
    
    def limpa_consumo(self):
        self.set_consumo([])

    def serializar(self):
        consumo_string = ""
        for j in self.get_consumo():
            consumo_string = "{}{}:".format(consumo_string, j)
        consumo_string = consumo_string[:-1]
        serialized_string = "{}/{}/{}/{}".format(self.get_numero(),self.get_categoria(),self.get_diaria(),consumo_string)
        
        return serialized_string
    
    def deserializar(self, string):
        split_string = string.strip().split("/")
        split_string[0] #numero
        split_string[1] #categoria
        split_string[2] #diaria
        split_string[3] #consumo
        
        self.set_numero(split_string[0])
        self.set_categoria(split_string[1])
        self.set_diaria(float(split_string[2]))
        consumoString = split_string[3]
        self.set_consumo(consumoString.strip().split(":"))

        return self