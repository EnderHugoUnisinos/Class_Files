class Pais:
    def __init__(self, codigo_iso, nome, populacao, dimensao_km2):
        self.codigo_iso = codigo_iso
        self.nome = nome
        self.populacao = populacao
        self.dimensao_km2 = dimensao_km2
        self.fronteira = []
    
    def getCodigoIso(self):
        return self.codigo_iso
    def setCodigoIso(self, codigo_iso):
        self.codigo_iso = codigo_iso
    
    def getNome(self):
        return self.nome
    def setNome(self, nome):
        self.nome = nome
    
    def getPopulacao(self):
        return self.populacao
    def setPopulacao(self, populacao):
        self.populacao = populacao

    def getDimensaoKm2(self):
        return self.dimensao_km2
    def setDimensaoKm2(self, dimensao_km2):
        self.dimensao_km2 = dimensao_km2

    def verificarIgualdadeSemantica(self, pais):
        if self.getCodigoIso() == pais.getCodigoIso:
            return True
        else:
            return False
        
    def densidadePopulacional(self):
        densidade = self.getPopulacao() / self.getDimensaoKm2() 
        return densidade
    
    def inserirFronteira(self, paises):
        self.fronteira = paises

    def verificarLimitrofe(self, pais):
        for i in self.fronteira:
            if i == pais:
                return True
        return False
    
    def paisesComuns(self, pais):
        lista = []
        for i in self.fronteira:
            for j in pais.fronteira:
                if i == j:
                    lista.append(i)
        return lista