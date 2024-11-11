def eratosth(n):
    """Eratosthenovo síto"""
    sito = [False, False] + [True] * (n-1)
    prvocisla = []

    i = 2
    while i <= n:
        if sito[i]:
            prvocisla.append(i)
            j = i * i      # stačí začít s násobky od kvadrátu "i"
            while j <= n:
                sito[j] = False
                j += i
        i = i + 1

    return prvocisla
