def ehPositivo(x):
    if(x >= 0):
        return True
    else:
        return False
try:
    x = float(input("Insira um numero: "))
except:
    print("That's not a valid number!")

if ehPositivo(x):
    print("O valor {} é positivo".format(x))
else:
    print("O valor {} é negativo".format(x))