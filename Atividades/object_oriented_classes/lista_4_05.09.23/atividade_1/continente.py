class Continente:
    def __init__(self, nome, paises = []):
        self.nome = nome
        self.paises = paises

    def adicionarPais(self, pais):
        self.paises.append(pais)
    
    def dimensaoTotal(self):
        total = 0
        for i in self.paises:
            total += i.getDimensaoKm2()
        return total
    def populacaoTotal(self):
        total = 0
        for i in self.paises:
            total += i.getPopulacao()
        return total
    def densidadeTotal(self):
        densidade = self.populacaoTotal() / self.dimensaoTotal()
        return densidade
    
    def maiorPopulacao(self):
        atual = self.paises[0]
        for i in self.paises:
            if i.getPopulacao() > atual.getPopulacao():
                atual = i
        return atual
    def menorPopulacao(self):
        atual = self.paises[0]
        for i in self.paises:
            if i.getPopulacao() < atual.getPopulacao():
                atual = i
        return atual
    def maiorDimensao(self):
        atual = self.paises[0]
        for i in self.paises:
            if i.getDimensaoKm2() > atual.getDimensaoKm2():
                atual = i
        return atual
    def menorDimensao(self):
        atual = self.paises[0]
        for i in self.paises:
            if i.getDimensaoKm2() < atual.getDimensaoKm2():
                atual = i
        return atual

    def razaoTerritorial(self):
        razao = self.maiorDimensao().getDimensaoKm2() / self.menorDimensao().getDimensaoKm2()
        return razao