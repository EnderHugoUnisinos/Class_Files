while True:
    try:
        base = float(input("insira of valor da base(cm): "))
        altura = float(input("insira of valor da altura(cm): "))
        profundidade = float(input("insira o valor da profundidade(cm): "))
        peso = float(input("insira o valor do peso(kg): "))
        distancia = float(input("insira a distancia percorrida(km): "))
        break
    except:
        print("Valor informado invalido, valores devem ser numeros reais!")
        continue
volume = base*altura*profundidade
frete = volume*peso*distancia/(7.5 * 10 ** 4)

print("\nVolume total da embalagem(cm^3): {:.2f}".format(volume))
print("Valor total do frete: R${:.2f}".format(frete))