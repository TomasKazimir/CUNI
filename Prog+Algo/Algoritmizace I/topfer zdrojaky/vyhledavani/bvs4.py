class Vrchol:
    """vrchol binárního stromu"""
    
    def __init__(self, x = None):
        self.info = x             # uložená hodnota
        self.levy = None          # levý syn
        self.pravy = None         # pravý syn

    def __str__(self):
        return str(self.info)

def pridej(p, x):
    """přidání hodnoty 'x' do BVS s kořenem ve vrcholu 'p' (pokud tam není)"""
    if p is None:
        p = Vrchol(x)
    elif x < p.info:
        p.levy = pridej(p.levy, x)
    elif x > p.info:
        p.pravy = pridej(p.pravy, x)
    return p

def hledej(p, x):
    """hledání hodnoty 'x' v BVS s kořenem ve vrcholu 'p'"""
    if p == None:
        return None
    elif x == p.info:
        return p
    elif x < p.info:
        return hledej(p.levy, x)
    else:
        return hledej(p.pravy, x)


v = Vrchol(10)
v.levy = Vrchol(5)
v.levy.levy = Vrchol(2)
v.levy.pravy = Vrchol(8)
v.pravy = Vrchol(20)
v.pravy.levy = Vrchol(15)
v.pravy.pravy = Vrchol(28)

print(hledej(v, 3))
pridej(v, 3)
print(hledej(v, 3))
