a = [9, 12, 12, 17, 17, 17, 25, 687, 777]
x = 17

i = 0                   # začátek úseku
j = len(a) - 1          # konec úseku
k = (i + j) // 2        # střed úseku
while a[k] != x and i <= j:
    if x > a[k]:
        i = k + 1
    else:
        j = k - 1
    k = (i + j) // 2
    
if x == a[k]:
    print("Je na pozici", k)
else:
    print("Není tam")
