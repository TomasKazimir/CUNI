def bin_int(s: str):
    """převod binárního zápisu čísla (string s) na číselnou hodnotu"""
    n = 0
    for i in range(len(s)):
        n = n * 2 + int(s[i])
    return n
