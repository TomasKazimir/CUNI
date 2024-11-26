halda = [None]     # prvek halda[0] nepoužijeme

def pridej(h, x):
    """do haldy 'h' přidá prvek 'x'"""
    h.append(x)
    j = len(h)-1
    while j > 1 and h[j] < h[j//2]:
        h[j], h[j//2] = h[j//2], h[j]
        j //= 2

def zrusmin(h):
    """z haldy 'h' odebere minimální prvek"""
    if len(h) == 1:
        return None                # prázdná halda
    zrus = h[1]
    h[1] = h[-1]
    del h[-1]
    j = 1
    while 2*j < len(h):
        n = 2*j
        if n < len(h)-1:
            if h[n+1] < h[n]:
                n += 1
        if h[j] > h[n]:
            h[j], h[n] = h[n], h[j]
            j = n
        else:
            break
    return zrus

pridej(halda, 4)
pridej(halda, 9)
pridej(halda, 2)
pridej(halda, 5)
pridej(halda, 1)
pridej(halda, 20)
pridej(halda, 90)
pridej(halda, 25)
pridej(halda, 15)
pridej(halda, 3)
print(zrusmin(halda))
print(zrusmin(halda))
print(zrusmin(halda))
print(zrusmin(halda))
print(zrusmin(halda))
print(zrusmin(halda))
print(zrusmin(halda))
print(zrusmin(halda))
print(zrusmin(halda))
print(zrusmin(halda))
print(zrusmin(halda))
