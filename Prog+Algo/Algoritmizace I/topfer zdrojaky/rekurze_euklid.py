def nsd(x, y):
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x


#  *Eukleidův algoritmus realizovaný rekurzivní funkcí*
#    - přesně kopíruje rekurzivní vztah pro NSD, na němž je Eukleidův algoritmus založen:
#             když X > Y :      NSD(X, Y) = NSD(X-Y, Y)
#             když X < Y :      NSD(X, Y) = NSD(X, Y-X)
#             když X = Y :      NSD(X, Y) = X

def nsd_recursion(x, y):
    if x > y:
        return nsd(x-y, y)
    elif x < y:
        return nsd(x, y-x)
    else:  # x = y
        return x

def nsd_recursion_modulo_optimisation(x, y):
    if y == 0:
        return x
    return nsd(y, x % y)