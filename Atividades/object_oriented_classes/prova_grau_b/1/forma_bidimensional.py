from forma import Forma
import math

class FormaBidimensional(Forma):
    def __init__(self) -> None:
        pass
    def getArea(self):
        pass
    def desenhar(self):
        pass
    def __str__(self) -> str:
        return "Forma Bidimensional"
    
class Circulo(FormaBidimensional):
    def __init__(self, raio, char, tamanho) -> None:
        self.raio = float(raio)
        self.caractere = char
        self.tamanho = int(tamanho)
    def __str__(self) -> str:
        return f"Forma Bidimensional\nCirculo\nArea: {self.getArea()}\n{self.desenhar()}"
        
    def getArea(self):
        area = math.pi * self.raio ** 2
        return area
    def desenhar(self):
        result = ""
        for i in range(self.tamanho):
            amount = 0
            for b in range(abs((round(self.tamanho/2))-i)):
                amount += 1
                result = f"{result} "
            for j in range(self.tamanho - amount):
                result = f"{result} {self.caractere}"
            result = f"{result}\n"
        return result
    
class Quadrado(FormaBidimensional):
    def __init__(self, lado, char, tamanho) -> None:
        self.lado = float(lado)
        self.caractere = char
        self.tamanho = int(tamanho)
    def __str__(self) -> str:
        return f"Forma Bidimensional\nQuadrado\nArea: {self.getArea()}\n{self.desenhar()}"
        
    def getArea(self):
        area = self.lado ** 2
        return area
    def desenhar(self):
        result = ""
        for i in range(self.tamanho):
            for j in range(self.tamanho):
                result = f"{result} {self.caractere}"
            result = f"{result}\n"
        return result

    
class Triangulo(FormaBidimensional):
    def __init__(self, lado, char, tamanho) -> None:
        self.lado = float(lado)
        self.caractere = char
        self.tamanho = int(tamanho)
    def __str__(self) -> str:
        return f"Forma Bidimensional\nTriangulo\nArea: {self.getArea()}\n{self.desenhar()}"
        
    def getArea(self):
        area = (self.lado * math.sqrt(3))/4
        return area
    def desenhar(self):
        result = ""
        for i in range(self.tamanho):
            for b in range(self.tamanho - i):
                result = f"{result} "
            for j in range(self.tamanho):
                result = f"{result} {self.caractere}"
                if j == i:
                    break
            result = f"{result}\n"
        return result