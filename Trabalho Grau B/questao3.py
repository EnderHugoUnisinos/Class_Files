ano = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]

def valorTotal():
    valorMeses = []
    for i in ano:
        valorMeses.append(sum(i))
    valorTotal = sum(valorMeses)
    for i in range(len(ano)):
        print(f"Total mês {i+1}: {valorMeses[i]}")
    print(f"\n Valor total vendido no ano: {valorTotal}")

valorTotal()