class Prvek:
    def __init__(self, x, dalsi):
        self.x = x
        self.dalsi = dalsi


def VytiskniLSS(p):
    print("LSS:", end=" ")
    while p != None:
        print(p.x, end=" ")
        p = p.dalsi
    print(".")


def NactiLSS():
    """cte cisla z radku, dokud nenacte prazdny radek"""
    prvni = None
    posledni = None
    r = input()
    while r != "":
        radek = r.split()
        if len(radek) == 0:  # protoze ten test r!="" v RCDX neukoncil cyklus!
            break
        for s in radek:
            p = Prvek(int(s), None)
            if prvni == None:
                prvni = p
            else:
                posledni.dalsi = p
            posledni = p
        r = input()
    return prvni


#################################################

def UnionDestruct(a: Prvek, b: Prvek):
    """ destruktivni sjednoceni dvou usporadanych seznamu
    * nevytvari zadne nove prvky, vysledny seznam bude poskladany z prvku puvodnich seznamu,
    * vysledek je MNOZINA, takze se hodnoty neopakuji """

    pomocny = Prvek(None, None)
    ocas = pomocny

    while a is not None or b is not None:
        if a is not None and (b is None or a.x < b.x):  # pridat z Acka
            ocas.dalsi = a
            ocas = ocas.dalsi
            print(ocas, a, ocas is a)
            a = a.dalsi
        elif b is not None and (a is None or a.x > b.x):  # pridat z Bcka
            ocas.dalsi = b
            ocas = ocas.dalsi
            b = b.dalsi
        else:  # pridat z obou
            ocas.dalsi = a
            ocas = ocas.dalsi
            a = a.dalsi
            b = b.dalsi

    return pomocny.dalsi


#################################################

VytiskniLSS(UnionDestruct(NactiLSS(), NactiLSS()))
