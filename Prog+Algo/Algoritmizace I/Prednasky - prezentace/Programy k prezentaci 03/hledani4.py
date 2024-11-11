a = [12, 25, 687, 9, 17, 12, 25, 777]
x = 25

i = 0
dalsi = True
while dalsi:
    if a[i] == x:
        dalsi = False
        print("Je na pozici", i)
    elif i == len(a)-1:
        dalsi = False
        print("Není tam")
    else:
        i += 1
