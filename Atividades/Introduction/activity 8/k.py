def is_float(string):
    if string.replace(".", "").isnumeric():
        return True
    else:
        return False
    
def str_to_float(string):
    floatValue = 0.0
    if(is_float(string)):
        floatValue = float(string)
    return floatValue

string = input("Insira string: ")
print(str_to_float(string))