class Produto:
    def __init__ (self, codigo = None, nome = None, preco = None):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

    def __str__(self) -> str:
        return f"Codigo: {self.get_codigo()}, Nome: {self.get_nome()}, Preço: {self.get_preco()}"

    def get_codigo(self):
        return self.codigo
    def get_nome(self):
        return self.nome
    def get_preco(self):
        return self.preco
    
    def set_codigo(self, codigo):
        self.codigo = codigo
    def set_nome(self, nome):
        self.nome = nome
    def set_preco(self, preco):
        self.preco = preco

    def serializar(self):
        serialized_string = "{}/{}/{}".format(self.get_codigo(),self.get_nome(),self.get_preco())
        return serialized_string

    def deserializar(self, string):
        split_string = string.strip().split("/")
        split_string[0] #codigo
        split_string[1] #nome
        split_string[2] #preco
        
        self.set_codigo(split_string[0])
        self.set_nome(split_string[1])
        self.set_preco(float(split_string[2].strip()))
        return self