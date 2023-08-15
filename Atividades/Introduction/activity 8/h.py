def segmentoDeTxt(seg, txt):
    seg = seg.lower()
    txt = txt.lower()

    if seg in txt:
        return True
    else:
        return False

seg = input("Insira segmento: ")
txt = input("Insira texto: ")

print(segmentoDeTxt(seg, txt))
