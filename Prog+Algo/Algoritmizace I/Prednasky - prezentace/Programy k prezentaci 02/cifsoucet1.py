def cifsoucet(x):
    """ciferný součet kladného celého čísla"""
    y = 0
    while x != 0:
        y += x % 10
        x //= 10
    return y


