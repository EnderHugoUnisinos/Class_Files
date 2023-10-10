class Elevador():
    def __init__(self, total_andares, capacidade):
        self.inicializar(total_andares, capacidade)
        
    def __str__(self):
        return f"Andar atual: {self.get_andar_atual()}, Total de andares: {self.get_total_andares()}, Capacidade maxima: {self.get_capacidade()}, Pessoas presentes: {self.get_pessoas_presentes()}"
        
    def __repr__(self):
        return f"Elevador:({self.get_andar_atual()},{self.get_total_andares()},{self.get_capacidade()},{self.get_pessoas_presentes()})"
    
    def inicializar(self, total_andares, capacidade):
        self.andar_atual = 0
        self.total_andares = int(total_andares)
        self.capacidade = int(capacidade)
        self.pessoas_presentes = 0
    
    def get_andar_atual(self):
        return self.andar_atual
    def get_total_andares(self):
        return self.total_andares
    def get_capacidade(self):
        return self.capacidade
    def get_pessoas_presentes(self):
        return self.pessoas_presentes
    
    def set_andar_atual(self, andar_atual):
        self.andar_atual = andar_atual
    def set_total_andares(self, total_andares):
        self.total_andares = total_andares
    def set_capacidade(self, capacidade):
        self.capacidade = capacidade
    def set_pessoas_presentes(self, pessoas_presentes):
        self.pessoas_presentes = pessoas_presentes
    
    def entrar(self):
        if self.get_pessoas_presentes() < self.get_capacidade():
            nova_quantidade = self.get_pessoas_presentes() + 1
            self.set_pessoas_presentes(nova_quantidade)
    
    def sair(self):
        if self.get_pessoas_presentes() > 0:
            nova_quantidade = self.get_pessoas_presentes() - 1
            self.set_pessoas_presentes(nova_quantidade)
            
    def subir(self):
        if self.get_andar_atual() < (self.get_total_andares() - 1):
            andar_acima = self.get_andar_atual() + 1
            self.set_andar_atual(andar_acima)
            
    def descer(self):
        if self.get_andar_atual() > 0:
            andar_abaixo = self.get_andar_atual() - 1
            self.set_andar_atual(andar_abaixo)