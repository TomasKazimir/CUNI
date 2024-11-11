def mocnina1(x, n):
    """výpočet x^n lineárně"""
    v = 1
    for i in range(n):
        v *= x
    return v
