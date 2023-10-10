import datetime

class Jogador():
    def __init__(self, nome, posicao, data_de_nascimento, nacionalidade, peso):
        self.nome = nome
        self.posicao = posicao
        self.data_de_nascimento = data_de_nascimento
        self.nacionalidade = nacionalidade
        self.peso = peso
    def __str__(self):
        return f"Nome: {self.get_nome()}, Posicão: {self.get_posicao()}, Data de nascimento: {self.get_data_de_nascimento()}, Nacionalidade: {self.get_nacionalidade()}, Peso: {self.get_peso()}"
        
    def __repr__(self):
        return f"Jogador({self.get_nome()},{self.get_posicao()},{self.get_data_de_nascimento()},{self.get_nacionalidade()},{self.get_peso()})"
    
    def get_nome(self):
        return self.nome
    def get_posicao(self):
        return self.posicao
    def get_data_de_nascimento(self):
        return self.data_de_nascimento
    def get_nacionalidade(self):
        return self.nacionalidade
    def get_peso(self):
        return self.peso
    
    def set_nome(self, nome):
        self.nome = nome
    def set_posicao(self, posicao):
        self.posicao = posicao
    def set_data_de_nascimento(self, data_de_nascimento):
        self.data_de_nascimento = data_de_nascimento
    def set_nacionalidade(self, nacionalidade):
        self.nacionalidade = nacionalidade
    def set_peso(self, peso):
        self.peso = peso
    
    def calcular_idade(self):
        data_atual = datetime.date.today()
        data_nasc_split = self.get_data_de_nascimento().split("-")
        data_atual_split = str(data_atual).split("-")
        dia = int(data_atual_split[2]) - int(data_nasc_split[0])
        mes = int(data_atual_split[1]) - int(data_nasc_split[1])
        ano = int(data_atual_split[0]) - int(data_nasc_split[2])
        if dia < 0:
            mes -= 1
        if mes < 0:
            ano -= 1
        return ano
    
    def calcular_tempo_para_aposentadoria(self):
        idade = int(self.calcular_idade())
        idade_aposentadoria = None
        match self.get_posicao():
            case "defesa":
                idade_aposentadoria = 40
            case "meio-campo":
                idade_aposentadoria = 38
            case "atacante":
                idade_aposentadoria = 35
        tempo = idade_aposentadoria - idade
        return tempo