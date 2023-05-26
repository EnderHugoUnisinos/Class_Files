def posicao(fraseA, fraseB):
    if fraseA == fraseB:
        print("As frases são iguais.")
    elif fraseA > fraseB:
        print("A primeira frase é posterior a segunda.")
    elif fraseA < fraseB:
        print("A primeira frase é anterior a segunda.")

fraseA = input("Digite a primeira frase: ")
fraseB = input("Digite a segunda frase: ")
posicao(fraseA, fraseB)