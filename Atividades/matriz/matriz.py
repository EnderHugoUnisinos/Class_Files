collumns = 6
lines = 4
matrix = [[],[],[],[]]
transMatrix = [[],[],[],[],[],[]]

def main():
    get_input()
    set_matrix()
    trans_matrix()
    display_matrix()

def get_input():
    for i in range(collumns):
        matrix[0].append(int(input()))

def set_matrix():
    for i in range(collumns):
        matrix[1].append(matrix[0][collumns-i-1])
        
    for i in range(collumns):
        matrix[2].append(matrix[0][i] + matrix[1][i])
    
    evenNumbers = []
    oddNumbers = []
    for i in range(collumns):
        if matrix[0][i]%2 == 0:
            evenNumbers.append(matrix[0][i])
        else:
            oddNumbers.append(matrix[0][i])
    for i in evenNumbers:
        matrix[3].append(i)
    for i in oddNumbers:
        matrix[3].append(i)

def trans_matrix():
    for i in range(collumns):
        for j in range(lines):
            transMatrix[i].append(matrix [j][i])

def display_matrix():
    for i in matrix:
        for j in i:
            print("{}\t".format(j),end="")
        print("\n")
    print("\n")
    for i in transMatrix:
        for j in i:
            print("{}\t".format(j),end="")
        print("\n")

if __name__ == '__main__':
    main()