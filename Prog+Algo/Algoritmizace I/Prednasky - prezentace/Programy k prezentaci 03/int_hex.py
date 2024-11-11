def int_hex(n):
    """převod čísla do šestnáctkové soustavy - obrácené Hornerovo schéma"""
    s = ""
    cifry = "0123456789ABCDEF"
    while n > 0:
        s = cifry[n % 16] + s          
        n //= 16
    return s
