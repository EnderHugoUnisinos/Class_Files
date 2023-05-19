x = input('Informe um caractere: ')

if x.isnumeric() and x.isalnum():
    print('Caractere {} é um numero'.format(x))
elif x >= 'A' and x <= 'Z':
    print('Caractere {} é uma letra maiuscula'.format(x))
elif x >= 'a' and x <= 'z':
    print('Caractere {} é uma letra minuscula'.format(x))
elif not x.isalnum():
    print('Caractere {} é um simbolo'.format(x))
else:
    print('Caractere {} não se encaixa em nenhuma categoria'.format(x))