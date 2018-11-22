def introduce():
    print("Hello, I'm Gittie")
    print("üdv innen a hátsó udvarból")

introduce()


def joke():
    szam = input("nyomj egy szamot, leginkabb az 1-t")
    if szam == '1':
        print("kacaghatsz")
    else:
        print('miért nem nyomtal 1-t?')
joke()




def add():
    a = 3
    b = 5
    c = a + b
    return c

print(add())

