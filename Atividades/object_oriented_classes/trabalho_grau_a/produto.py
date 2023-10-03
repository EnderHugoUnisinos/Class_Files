class Produto:
    def __init__ (self, codigo = None, nome = None, preco = None):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

    def serializar(self):
        serialized_string = "{}/{}/{}".format(self.codigo,self.nome,self.preco)
        return serialized_string

    def deserializar(self, string):
        split_string = string.strip().split("/")
        split_string[0] #codigo
        split_string[1] #nome
        split_string[2] #preco
        
        self.codigo = split_string[0]
        self.nome = split_string[1]
        self.preco = float(split_string[2].strip())
        return self