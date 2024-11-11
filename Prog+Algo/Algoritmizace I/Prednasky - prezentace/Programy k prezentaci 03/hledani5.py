a = [12, 25, 687, 9, 17, 12, 25, 777]
x = 25

a.append(x)         # přidat zarážku
i = 0
while a[i] != x:
    i += 1
del a[len(a)-1]     # zrušit zarážku

if i == len(a):
    print("Není tam")
else:
    print("Je na pozici", i)
    
