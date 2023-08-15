extensoDictionary = {1: 'Um', 2: 'Dois', 3: 'Três', 4: 'Quatro', 5: 'Cinco', 6: 'Seis', 7: 'Sete', 8: 'Oito', 9: 'Nove', 
           10: 'Dez', 11: 'Onze', 12: 'Doze', 13: 'Treze', 14: 'Quatorze', 15: 'Quinze', 16: 'Dezesseis', 17: 'Dezessete', 18: 'Dezoito', 19: 'Dezenove', 
           20: 'Vinte', 30: 'Trinta', 40: 'Quarenta', 50: 'Cinquenta', 60: 'Sessenta', 70: 'Setenta', 80: 'Oitenta', 90: 'Noventa', 
           0: 'Zero'}

def num_to_ext(n):
    extenso = ""
    try:
         extenso = extensoDictionary[n]
    except KeyError:
        try:
            extenso = extensoDictionary[n-n%10] + " e " + extensoDictionary[n%10].lower()
        except KeyError:
            print('Numero informado é invalido...')
            main()
    return extenso

def main():
    while True:
        try:
            num = int(input("Insira numero inteiro de 0 - 99: "))
            if num < 100:
                break
        except:
            print("Numero informado é invalido...")
            continue
    print(num_to_ext(num))

if __name__=='__main__':  
    main()  