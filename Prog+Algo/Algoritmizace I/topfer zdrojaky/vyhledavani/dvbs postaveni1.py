class Vrchol:
    """vrchol binárního stromu"""
    
    def __init__(self, x = None):
        self.info = x             # uložená hodnota
        self.levy = None          # levý syn
        self.pravy = None         # pravý syn

def postav(n):
    """postavení dokonale vyváženého binárního stromu s 'n' vrcholy"""
    if n == 0:
        return None
    p = Vrchol(1)
    p.levy = postav((n-1)//2)
    p.pravy = postav(n-1 - (n-1)//2)
    return p


postav(20)
