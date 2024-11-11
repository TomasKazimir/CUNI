a = [12, 25, 687, 9, 17, 12, 25, 777]
x = 25

i = 0
while i < len(a) and a[i] != x:
    i += 1

if i == len(a):
    print("Není tam")
else:
    print("Je na pozici", i)

