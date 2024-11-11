def int_bin(n):
    """převod čísla do dvojkové soustavy - obrácené Hornerovo schéma"""
    s = ""
    while n > 0:
        s = str(n % 2) + s
        n //= 2
    return s
