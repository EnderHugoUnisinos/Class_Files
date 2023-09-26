class Produto:
    def __init__ (self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

    def serializar(self):
        serialized_string = "{}/{}/{}".format(self.codigo,self.nome,self.preco)
        return serialized_string

    def deserializar(self):
        pass