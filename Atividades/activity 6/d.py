from textwrap import wrap

def horaParaFloat(h,m,s):
    floatTime = "{}{}{}".format(h,m,s)
    return floatTime
def floatParaHora(h,m,s):
    stringTime = "{}:{}:{}".format(h,m,s)
    return stringTime

convertTo = input("Choose conversion type float to string[fts] or string to float[stf]: ")
match convertTo:
    case "fts":
        while True:
            time = input("Insert a time in the format (hhmmss): ")
            time = wrap(time, 2)
            try:
                separatedTime = [eval(i) for i in time]
            except:
                print("Time informed is invalid")
                continue
            break
        stringTime = floatParaHora(time[0],time[1],time[2])
        print(stringTime)
    case "stf":
        while True:
            time = input("Insert a time in the format (hh:mm:ss): ")
            time = time.split(":")
            try:
                separatedTime = [eval(i) for i in time]
            except:
                print("Time informed is invalid")
                continue
            break
        floatTime = horaParaFloat(time[0],time[1],time[2])
        print(floatTime)
