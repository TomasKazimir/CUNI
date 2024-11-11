def merge(a, zac, stred, kon, temp):
    """ 
      sleje a[zac..stred] s a[stred+1..kon]
      do a[zac..kon] pomocí temp[zac..kon]
    """
    i = zac             # začátek prvního úseku
    j = stred+1         # začátek druhého úseku
    k = zac             # začátek výsledného seznamu
    
    # sleje a[zac..stred] s a[stred+1..kon] do temp[zac..kon] 
    while i <= stred and j <= kon: 
        if a[i] < a[j]:
            temp[k] = a[i] 
            i += 1
        else: 
            temp[k] = a[j] 
            j += 1
        k += 1

    if i <= stred:      # zbytek prvního úseku
        temp[k:kon+1] = a[i:stred+1]
    else:               # zbytek druhého úseku
        temp[k:kon+1] = a[j:kon+1]
        
    # výsledek zkopíruje zpět do seznamu a
    a[zac:kon+1] = temp[zac:kon+1]
        
def mergesort(a):
    """
      třídění sléváním - iterativní verze
    """
    n = len(a)          # délka vstupního seznamu
    temp = [None] * n   # alokuje pomocný seznam
    
    # postupně slévá sousední úseky délek 1, 2, 4, ...
    for usek in [2**i for i in range(n)]: 
        for zacatek in range(0, n-usek, 2*usek):
            stred = zacatek + usek - 1
            konec = min(stred + usek, n-1)
            merge(a, zacatek, stred, konec, temp)

p = [5, 22, 4, 0, 5, -77, -14, 0, 0, 1, -80]
mergesort(p)
print(p)
