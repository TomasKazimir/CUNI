def prvocislo(n):
    """
      test prvočíselnosti, předpoklad n > 1
    """
    if n % 2 == 0:
        return n == 2       # jediné sudé prvočíslo: 2
    d = 3
    while d * d <= n:       # místo volání sqrt(n)
        if n % d == 0:
            return False
        d += 2
    return True

