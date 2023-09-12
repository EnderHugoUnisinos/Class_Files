import csv

class Pessoa:
    def __init__ (self, id, nome, sexo, idade, altura, peso):
        self.id = id
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.altura = altura
        self.peso = peso
    
    def get_nome(self):
        return self.nome
    def set_nome(self, nome):
        self.nome = nome
    
    def get_sexo(self):
        return self.sexo
    def set_sexo(self, sexo):
        self.sexo = sexo
    
    def get_idade(self):
        return self.idade
    def set_idade(self, idade):
        self.idade = idade
    
    def get_altura(self):
        return self.altura
    def set_altura(self, altura):
        self.altura = altura

    def get_peso(self):
        return self.peso
    def set_peso(self, peso):
        self.peso = peso
    
    def get_id(self):
        return id
    def set_id(self, id):
        self.id = id

    def visualizar(self):
        return "Nome: {}\nSexo: {}\nIdade: {}\nAltura: {}\nPeso: {}\n".format(self.nome,self.sexo,self.idade,self.altura,self.peso)
    
    def carregar(self, nomeArquivo):
        with open(nomeArquivo, "r") as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                if row[0] == str(self.get_id()):
                    self.set_nome(row[1])
                    self.set_idade(row[2])
                    self.set_altura(row[3])
                    self.set_peso(row[4])
                    self.set_sexo(row[5])

    def salvar(self, nomeArquivo):
        file_content = []
        with open(nomeArquivo, "r") as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                file_content.append([row[0],row[1],row[2],row[3],row[4],row[5]])
        modified = False
        for i in range(len(file_content)):
            if str(file_content[i][0]) == str(self.id):
                modified = True
                file_content[i] = [self.id, self.nome, self.idade, self.altura, self.peso, self.sexo]
        if modified == False:
            file_content.append([self.id, self.nome, self.idade, self.altura, self.peso, self.sexo])
        with open(nomeArquivo, "w") as file:
            for i in range(len(file_content)):
                file.write(str(file_content[i][0]) + ",")
                file.write(str(file_content[i][1]) + ",")
                file.write(str(file_content[i][2]) + ",")
                file.write(str(file_content[i][3]) + ",")
                file.write(str(file_content[i][4]) + ",")
                file.write(str(file_content[i][5]))
                file.write("\n")