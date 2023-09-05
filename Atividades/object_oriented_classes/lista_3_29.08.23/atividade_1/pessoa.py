class Pessoa:
    def __init__(self, nome: str, sexo: str, corOlhos: str, pai= None, mae = None):
        self.nome = nome
        self.sexo = sexo
        self.corOlhos = corOlhos
        self.pai = pai
        self.mae = mae

    def geraPessoa(self, nome: str, sexo: str, pai):
        if self.getSexoStr() == "F" and pai.getSexoStr() == "M":
            dictCorDominante = {'C':2,'V':1,'A':0}
            corPai = pai.getCorOlhosStr()
            corMae = self.getCorOlhosStr()
            if dictCorDominante[corMae] > dictCorDominante[corPai]:
                corOlhos = corMae
            else:
                corOlhos = corPai    
            pessoaGerada = Pessoa(nome, sexo, corOlhos, pai, self)
            return pessoaGerada
        else:
            print("(Mãe deve ser do sexo feminino e pai do sexo masculino.)")
            return None

    def setSexo(self, sexo: str):
        if sexo in ['M', 'F']:
            self.sexo = sexo

    def setCorOlhos(self, corOlhos: str):
        if corOlhos in ['C','V','A']:
            self.corOlhos = corOlhos

    def getNome(self) -> str:
        return self.nome

    def getSexoStr(self) -> str:
        return self.sexo

    def getCorOlhosStr(self) -> str:
        return self.corOlhos

    def imprimeDados(self):
        dictSexo = {'M':'Masculino', 'F':'Feminino'}
        dictCorOlhos = {'C':'Castanho','V':'Verde','A':'Azul'}

        nome = self.nome
        sexo = dictSexo[self.sexo]
        corOlhos = dictCorOlhos[self.corOlhos]
        nomePai = None
        nomeMae = None
        if self.pai:
            nomePai = self.pai.getNome()
        if self.mae:
            nomeMae = self.mae.getNome()
        
        print("{}\t{}\t{}\t{}\t{}\t".format(nome, sexo, corOlhos, nomePai, nomeMae))

    def verificarIgualdadeSemantica(self, pessoa):
        if self.mae != None and pessoa.pai != None:
            if self.getNome() == pessoa.getNome() and self.mae.getNome() == pessoa.mae.getNome():
                return True
        return False
    
    def verificarFraternidade(self, pessoa):
        if self.mae != None and pessoa.pai != None:
            if self.mae == pessoa.mae or self.pai == pessoa.pai:
                return True
        return False

    def verificarAntecedente(self, pessoa):
        parent = self
        while parent != None:
            if parent.pai == pessoa:
                return True
            parent = parent.pai
        while parent != None:
            if parent.mae == pessoa:
                return True
            parent = parent.mae
        return False