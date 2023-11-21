from forma import Forma
import math

class FormaTridimensional(Forma):
    def __init__(self) -> None:
        pass
    def __str__(self) -> str:
        return "Forma Tridimensional"
    def getArea(self):
        pass
    def getVolume(self):
        pass
    
class Esfera(FormaTridimensional):
    def __init__(self, raio) -> None:
        self.raio = float(raio)
    def __str__(self) -> str:
        return f"Forma Tridimensional\nEsfera\nArea: {self.getArea()}\nVolume: {self.getVolume()}"
    def getArea(self):
        area = 4 * math.pi * self.raio ** 2
        return area
    def getVolume(self):
        volume = (4 * math.pi * self.raio ** 3)/3
        return volume
    
class Cubo(FormaTridimensional):
    def __init__(self, aresta) -> None:
        self.aresta = float(aresta)
    def __str__(self) -> str:
        return f"Forma Tridimensional\nCubo\nArea: {self.getArea()}\nVolume: {self.getVolume()}"
    def getArea(self):
        area = 6 * self.aresta ** 2
        return area
    def getVolume(self):
        volume = self.aresta ** 3
        return volume
    
class Tetraedro(FormaTridimensional):
    def __init__(self, aresta) -> None:
        self.aresta = float(aresta)
        self.area_b = ((float(aresta) ** 2) * math.sqrt(3))/4
        self.altura = (float(aresta) * math.sqrt(6))/3
    def __str__(self) -> str:
        return f"Forma Tridimensional\nTetraedro\nArea: {self.getArea()}\nVolume: {self.getVolume()}"

    def getArea(self):
        area = 4*((self.aresta * math.sqrt(3))/4)
        return area
    
    def getVolume(self):
        volume = (1/3)*self.area_b*self.altura
        return volume