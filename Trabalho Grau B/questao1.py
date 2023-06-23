def computarPalavra(palavra):
    caracteres = len(palavra)
    priLetra = palavra[0]
    ultLetra = palavra[-1]
    maiuscula = f"{palavra}".upper()
    x = input("Insira o caractere a ser testado: ")
    print(f"""
    Palavra: {palavra}
    Numero de caracteres: {caracteres}
    Palavra maiuscula: {maiuscula}
    Primeira letra: {priLetra}
    Ultima Letra: {ultLetra}
    """)
    if x in palavra:
        print(f"""
        Caractere \"{x}\" FOI encontrado na palavra \"{palavra}\"
        """)
    else:
        print(f"""
        Caractere \"{x}\" NÃO foi encontrado na palavra \"{palavra}\"
        """)

computarPalavra(input("Insira a palavra a ser testada: "))