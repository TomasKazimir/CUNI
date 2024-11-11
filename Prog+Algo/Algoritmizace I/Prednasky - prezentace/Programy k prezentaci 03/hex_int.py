def hex_int(s):
    """převod hexadecimálního zápisu čísla (string s) na číselnou hodnotu"""
    cifry = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15,
             'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
    n = 0
    for i in range(len(s)):
        if s[i] in "0123456789":
            n = n * 16 + int(s[i])
        else:
            n = n * 16 + cifry[s[i]]
    return n
