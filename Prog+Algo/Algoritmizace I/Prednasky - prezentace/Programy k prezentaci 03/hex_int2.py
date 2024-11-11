def hex_int(s):
    """převod hexadecimálního zápisu čísla (string s) na číselnou hodnotu"""
    cifry = "0123456789ABCDEF"
    n = 0
    for i in range(len(s)):
        n = n * 16 + cifry.index(s[i])
    return n
