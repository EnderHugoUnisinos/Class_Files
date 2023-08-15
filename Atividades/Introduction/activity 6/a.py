
result = 0.0
x = 0.0
y = 0.0
    
def addition(x,y):
    result = x+y
    return result
def subtraction(x,y):
    result = x-y
    return result
def multiplication(x,y):
    result = x*y
    return result
def division(x,y):
    result = x/y
    return result

try:
    x = float(input('Insert the first number: '))
except:
    print("That's not a valid number")

type = input("Insert the type of operation (*|/|+|-): ")

try:
    y = float(input('Insert the second number: '))
except:
    print("That's not a valid number")

match type:

    case "*":
        result = multiplication(x,y)
    case "/":   
        result = division(x,y)
    case "+":   
        result = addition(x,y)
    case "-":
        result = subtraction(x,y)
    case _:
        print("The type of operation is not valid")

print("\nOperation: {} {} {}\nResult: {}".format(x,type,y,result))