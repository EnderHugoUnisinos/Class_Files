from datetime import date

class Imposto:
    def __init__(self, nome, nascimento, profissao, escolaridade, renda_mensal, numero_dependentes):
        self.nome = nome
        self.nascimento = nascimento
        self.profissao = profissao
        self.escolaridade = escolaridade
        self.renda_mensal = renda_mensal
        self.numero_dependentes = numero_dependentes

    def __str__(self):
        return f"""
    Nome do contribuinte: \t{self.nome}
    Ano de nascimento: \t{self.nascimento}
    Profissão: \t{self.profissao}
    Escolaridade: \t{self.escolaridade}
    Renda mensal: \t{self.renda_mensal}
    Número de dependentes: \t{self.numero_dependentes}
    Idade: \t{self.idade()}
    Renda anual: \t{self.renda_anual()}
    Renda per capita mensal: \t{self.renda_per_capita_mensal()}
    Aliquota IR maxima: \t{self.aliquota_IR_maxima()}
    Aliquota IR efetiva: \t{self.aliquota_IR_efetiva()}
    Valor IR devido: \t{self.valor_IR_devido()}"""

    def idade(self):
        birth_date_list = self.nascimento.split("-")
        today = date.today()
        today_list = [today.strftime("%d"),today.strftime("%m"),today.strftime("%Y")]
        day_age = int(today_list[0]) - int(birth_date_list[0])
        month_age = int(today_list[1]) - int(birth_date_list[1]) 
        year_age = int(today_list[2]) - int(birth_date_list[2]) 
        
        if (month_age < 0 or (day_age < 0 and month_age == 0)):
            year_age -= 1
        return year_age
        
    def renda_anual(self):
        renda_anual = float(self.renda_mensal) * 12
        return renda_anual
    
    def renda_per_capita_mensal(self):
        if self.numero_dependentes != "0":
            renda_per_capita_mensal = float(self.renda_mensal) / float(self.numero_dependentes)
        else: 
            renda_per_capita_mensal = float(self.renda_mensal)
        return renda_per_capita_mensal
    
    def aliquota_IR_maxima(self):
        aliquota_faixas = [1900,2820,3740,4660]
        aliquota_porcent = [0, 0.075,0.15,0.225,0.275]
        renda = float(self.renda_mensal)
        faixa = 0
        for i in aliquota_faixas:
            if renda < i:
                break
            else:
                faixa += 1
        al_IR_maxima = aliquota_porcent[faixa]
        return al_IR_maxima
            
    
    def aliquota_IR_efetiva(self):
        aliquota_faixas = [1900,2820,3740,4660]
        aliquota_porcent = [0, 0.075,0.15,0.225,0.275]
        renda = float(self.renda_mensal) - (float(self.numero_dependentes)*190)
        faixa = 0
        for i in aliquota_faixas:
            if renda < i:
                break
            faixa += 1
        al_IR_efetiva = aliquota_porcent[faixa]
        return al_IR_efetiva
    
    def valor_IR_devido(self):
        valor_devido = float(self.renda_mensal) * self.aliquota_IR_efetiva()
        return valor_devido
        
