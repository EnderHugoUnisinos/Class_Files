class Quarto:
    def __init__ (self, __numero = None, __categoria = None, __diaria = None, __consumo = []):
        self.numero = __numero
        self.categoria = __categoria
        self.diaria = __diaria
        
        #consumo provavelmente se encaixa melhor em reserva, mas vamos manter aqui de acordo com o diagrama
        self.consumo = __consumo
    
    def __str__(self) -> str:
        return f'Numero: {self.getNumero()}, Categoria: {self.getCategoria()}, Diaria: {self.getDiaria()}'     
    def __repr__(self):
        return f'Quarto({self.getNumero()},{self.getCategoria()},{self.getDiaria()},{self.getConsumo()})'
    
    #redundancy to follow the code schematics
    def toString(self):
        return f'Numero: {self.getNumero()}, Categoria: {self.getCategoria()}, Diaria: {self.getDiaria()}'

    def getNumero(self):
        return self.numero
    def getCategoria(self):
        return self.categoria
    def getDiaria(self):
        return self.diaria
    def getConsumo(self):
        return self.consumo
    
    def setNumero(self, numero):
        self.numero = numero
    def setCategoria(self, categoria):
        self.categoria = categoria
    def setDiaria(self, diaria):
        self.diaria = diaria
    def setConsumo(self, consumo):
        self.consumo = consumo

    def adicionaConsumo(self, codigo):
        self.consumo.append(codigo)
    def listaConsumo(self, produtos):
        listaConsumo = []
        for i in self.getConsumo():
            for j in produtos:
                if j.getCodigo() == i:
                    listaConsumo.append(j)
        return listaConsumo
    def valorTotalConsumo(self, produtos):
        totalValue = 0
        for i in self.getConsumo():
            for j in produtos:
                if j.getCodigo() == i:
                    totalValue += j.getPreco()
        
        return totalValue
    def limpaConsumo(self):
        self.setConsumo([])

    def serializar(self):
        consumoString = ""
        for j in self.getConsumo():
            consumoString = "{}{}:".format(consumoString, j)
        consumoString = consumoString[:-1]
        serializedString = "{}/{}/{}/{}".format(self.getNumero(),self.getCategoria(),self.getDiaria(),consumoString)
        
        return serializedString
    def deserializar(self, string):
        splitString = string.strip().split("/")
        splitString[0] #numero
        splitString[1] #categoria
        splitString[2] #diaria
        try:
            splitString[3] #consumo
        except:
            splitString.append("") 
        self.setNumero(splitString[0])
        self.setCategoria(splitString[1])
        self.setDiaria(float(splitString[2]))
        consumoString = splitString[3]
        self.setConsumo(consumoString.strip().split(":"))

        return self