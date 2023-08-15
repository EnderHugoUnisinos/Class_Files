import math

radius = int(input("Circle radius: "))
diameter = radius * 2
circumference = math.pi * radius 
area = 2 * math.pi * radius ** 2
print("\nRadius: {}\nDiameter: {}\nCircumference: {}\nArea: {}".format(radius, diameter, circumference, area))