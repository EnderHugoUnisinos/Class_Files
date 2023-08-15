convert = input("Temperature converter, what type do you wish to convert? Celsius/Fahrenheit (C/F)")
if convert == "C" or convert == "c":
    celcius = float(input("Celcius: "))
    fahrenheit = celcius * 1.8 + 32
if convert == "F" or convert == "f":
    fahrenheit = float(input("Fahrenheit: "))
    celcius = (fahrenheit - 32) / 1.8
print("{}Cº : {}Fº".format(celcius, fahrenheit))