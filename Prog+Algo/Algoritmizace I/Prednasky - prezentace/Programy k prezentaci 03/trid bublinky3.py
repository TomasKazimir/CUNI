a = [28, 16, 1, 43, 16, 7, 20, 18, 35]

def trid_bublinkove(a):
    vymena = len(a)-1
    while vymena > 0:
        pruchod = vymena            # kam až procházíme seznam
        vymena = 0
        for j in range(pruchod):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                vymena = j          # místo poslední výměny

trid_bublinkove(a)
print(a)

