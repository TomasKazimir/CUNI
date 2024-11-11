def mocnina2(x, n):
    """výpočet x^n rychleji"""
    v = 1
    while n > 0:
        if n % 2 == 1:
            v *= x
        x *= x
        n //= 2
    return v
