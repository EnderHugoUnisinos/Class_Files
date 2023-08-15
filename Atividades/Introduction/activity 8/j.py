def str_to_int(string):
    result = 0
    if(string.isdecimal()):
        result = int(string)
    return result

string = input("Insira string: ")
print(str_to_int(string))