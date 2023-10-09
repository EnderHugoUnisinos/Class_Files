class Produto:
    def __init__ (self, codigo = None, nome = None, preco = None):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

    def __str__(self) -> str:
        return f"Codigo: {self.getCodigo()}, Nome: {self.getNome()}, Preço: {self.getPreco()}"

    def getCodigo(self):
        return self.codigo
    def getNome(self):
        return self.nome
    def getPreco(self):
        return self.preco
    
    def setCodigo(self, codigo):
        self.codigo = codigo
    def setNome(self, nome):
        self.nome = nome
    def setPreco(self, preco):
        self.preco = preco

    def serializar(self):
        serializedString = "{}/{}/{}".format(self.getCodigo(),self.getNome(),self.getPreco())
        return serializedString

    def deserializar(self, string):
        splitString = string.strip().split("/")
        splitString[0] #codigo
        splitString[1] #nome
        splitString[2] #preco
        
        self.setCodigo(splitString[0])
        self.setNome(splitString[1])
        self.setPreco(float(splitString[2].strip()))
        return self