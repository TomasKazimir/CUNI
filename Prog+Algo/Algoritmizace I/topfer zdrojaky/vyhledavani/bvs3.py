﻿class Vrchol:
    """vrchol binárního stromu"""
    
    def __init__(self, x = None):
        self.info = x             # uložená hodnota
        self.levy = None          # levý syn
        self.pravy = None         # pravý syn

    def __str__(self):
        return str(self.info)

def hledej(p, x):
    """hledání hodnoty 'x' v BVS s kořenem ve vrcholu 'p'"""
    if p == None or x == p.info:
        return p
    return hledej(p.levy, x) \
        if x < p.info \
        else hledej(p.pravy, x)


v = Vrchol(10)
v.levy = Vrchol(5)
v.levy.levy = Vrchol(2)
v.levy.pravy = Vrchol(8)
v.pravy = Vrchol(20)
v.pravy.levy = Vrchol(15)
v.pravy.pravy = Vrchol(28)

print(hledej(v, 28))