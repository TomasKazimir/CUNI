class Vrchol:
    """vrchol binárního stromu"""
    
    def __init__(self, x = None):
        self.info = x             # uložená hodnota
        self.levy = None          # levý syn
        self.pravy = None         # pravý syn

def strom(a: list, x: int, y: int):
    """
      postavení dokonale vyváženého binárního stromu
      s hodnotami z uspořádaného seznamu "a"
      v úseku od indexu "x" po index "y" včetně
    """
    if x > y:
        return None
    p = Vrchol(a[(x+y)//2])
    p.levy = strom(a, x, (x+y)//2 - 1)
    p.pravy = strom(a, (x+y)//2 + 1, y)
    return p


a=[3, 7, 9, 12, 14, 16, 24, 26, 28, 33]
strom(a, 0, 8)
