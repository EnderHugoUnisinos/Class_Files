Matrix = []
lin = 10
col = 10
for i in range(lin):
    Matrix.append([0] * col)

for i in range(lin):
    for j in range(col):
        Matrix[i][j] = i + (j/col)

#Matriz Completa
for l in Matrix:
    print(l)

#Diagonal Primaria
print("\nDiagonal Primaria: ", end= '')
for i in range(lin):
    print(Matrix[i][i], end=' ')

#Diagonal Secundaria
print("\nDiagonal Secundaria: ", end= '')
for i in range(lin):
    print(Matrix[i][col-1-i], end=' ')

#Bordas
Bordas = []
for i in range(lin):
    Bordas.append([0] * col)
    
for i in range(lin):
    for j in range(col):
        if(i == 0 or i == (lin-1) or j == 0 or j == (lin-1)):
            Bordas[i][j] = Matrix[i][j]

for l in Bordas:
    print(f"{l}")

