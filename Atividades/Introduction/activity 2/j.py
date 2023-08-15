import math

catetoAdj = int(input("Cateto adjacente: "))
catetoOpos = int(input("Cateto oposto: "))
hipotenusa = math.sqrt(catetoOpos ** 2 + catetoAdj ** 2)
perimetro = hipotenusa + catetoAdj + catetoOpos
area = catetoAdj * catetoOpos / 2
seno = catetoOpos/hipotenusa
cosseno = catetoAdj/hipotenusa
tangente = catetoOpos/catetoAdj

print("\nCateto adjacente: {}\nCateto oposto: {}\n Hipotenusa: {}\nPerimetro: {}\nArea: {}\n Seno: {}\nCosseno: {}\n Tangente: {}".format(catetoAdj, catetoOpos, hipotenusa, perimetro, area, seno, cosseno, tangente))