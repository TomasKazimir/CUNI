from math import sqrt

def prvocislo(n):
    """
      test prvočíselnosti, předpoklad n > 1
    """
    # stačí prověřit dělitele do odmocniny z n
    for d in range(2, int(sqrt(n))+1):  
        if n % d == 0:      # pokud d | n
            return False    # n není prvočíslo
    return True
