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

    prvni = Prvek(None, None)
    posledni = Prvek(None, None)
    while a is not None and b is not None:
        p = Prvek(None, None)
        if a.x == b.x:
            p.x = a.x
            a = a.dalsi
            b = b.dalsi
        elif a.x < b.x:
            p.x = a.x
            a = a.dalsi
        else:
            p.x = b.x
            b = b.dalsi
        if prvni.dalsi is None:
            prvni.dalsi = p
        else:
            posledni.dalsi = p

        posledni = p
    if a is not None:
        posledni.dalsi = a
    elif b is not None:
        posledni.dalsi = b
    if prvni.dalsi is None:
        return posledni.dalsi
    return prvni.dalsi


#################################################

VytiskniLSS(UnionDestruct(NactiLSS(), NactiLSS()))
