
vetor = [33,5,54,41,3,16,19,8,87,93]

def menorValor(vetor):
    x = vetor[0]
    for i in vetor:
        if i < x:
            x = i
    return x

def maiorValor(vetor):
    x = vetor[0]
    for i in vetor:
        if i > x:
            x = i
    return x

def mediaValoresPares(vetor):
    vetorTemporario = []
    for i in vetor:
        if (i%2) == 0:
            vetorTemporario.append(i)
    soma = 0
    for i in vetorTemporario:
        soma += i
    try:
        media = soma / len(vetorTemporario)
    except:
        media = 0
    return media


def Main():
    menor = menorValor(vetor)
    maior = maiorValor(vetor)
    media = mediaValoresPares(vetor)
    print(f"Menor valor: {menor}")
    print(f"Maior valor: {maior}")
    print(f"Media de valores pares: {media:.2f}")


if __name__ == "__main__":
    Main()