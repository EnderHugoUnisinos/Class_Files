import math

def RootP(a,b,c):
    try:
        xP = (b + math.sqrt(b**2-4*a*c))/(2*a)
    except:
        print("O resultado corresponde a um numero imaginario")
    return xP

def RootN(a,b,c):
    try:
        xN = (b - math.sqrt(b**2-4*a*c))/(2*a)
    except:
        print("O resultado corresponde a um numero imaginario")
    return xN

while True:
    try:
        a = float(input("Insert the A value of the expression: "))
    except:
        print("Not a valid number")
        continue
    break
while True:
    try:
        b = float(input("Insert the B value of the expression: "))
    except:
        print("Not a valid number")
        continue
    break
while True:
    try:
        c = float(input("Insert the C value of the expression: "))
    except:
        print("Not a valid number")
        continue
    break
xP = RootP(a,b,c)
xN = RootN(a,b,c)

print("Roots of the expression are: {} and {}".format(xP,xN))