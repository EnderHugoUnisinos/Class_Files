import csv

data = []

def main():
    read_file()
    display_file()
    quotas()
    best()
    shortest_lines()

def read_file():
    file = "data.csv"
    with open(file, "r") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if row[0] != "linguagem" :
                data.append({
                    "linguagem" : row[0],
                    "cpu" : int(row[1]),
                    "memoria" : float(row[2]),
                    "tempo" : int(row[3]),
                    "linhas" : int(row[4])
                })

def display_file():
    for i in data:
        print("{}\t{}\t{:.2f}\t{}\t{}\t".format(i["linguagem"],i["cpu"],i["memoria"],i["tempo"],i["linhas"]))
    print("\n")

def quotas():
    averages = {"cpu" : 0,"memoria" : 0.0,"tempo" : 0,"linhas":0}
    for i in data:
        averages["cpu"] += i["cpu"]
        averages["memoria"] += i["memoria"]
        averages["tempo"] += i["tempo"]
        averages["linhas"] += i["linhas"]
    averages["cpu"] = averages["cpu"] / len(data)
    averages["memoria"] = averages["memoria"] / len(data)
    averages["tempo"] = averages["tempo"] / len(data)
    averages["linhas"] = averages["linhas"] / len(data)
    print("Média de CPU: \t\t{}".format(averages["cpu"]))
    print("Média de memoria: \t{}".format(averages["memoria"]))
    print("Média de tempo: \t{}".format(averages["tempo"]))
    print("Média de linhas: \t{}".format(averages["linhas"]))

def best():
    best = {"linguagem" : "","cpu" : 0,"memoria" : 0.0,"tempo" : 0,"linhas" : ""}
    bestResult = 0
    for i in data:
        currentResult = 10**6 / (i["cpu"]*100+i["memoria"]+i["tempo"]+i["linhas"])
        if bestResult == 0:
            best = i
            bestResult = currentResult
        elif currentResult < bestResult:
            best = i
            bestResult = currentResult
    print("Melhor desempenho: \t{}\t{}\t{:.2f}\t{}\t{}\t".format(best["linguagem"],best["cpu"],best["memoria"],best["tempo"],best["linhas"]))
     
    


def shortest_lines():
    best = {"linguagem" : "","cpu" : 0,"memoria" : 0.0,"tempo" : 0,"linhas" : data[0]["linhas"]}
    for i in data:
        if i["linhas"] < best["linhas"]:
            best = i
    print("Menos linhas: \t\t{}\t{}\t{:.2f}\t{}\t{}\t".format(best["linguagem"],best["cpu"],best["memoria"],best["tempo"],best["linhas"]))

if __name__ == "__main__":
    main()
