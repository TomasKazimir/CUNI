a = [12, 25, 687, 9, 17, 12, 25, 777]
x = 25

j = -1
for i in range(len(a)):
    if a[i] == x:
        j = i

if j == -1:
    print("Není tam")
else:
    print("Je na pozici", j)

