a = [2, 3, 9, 4, 1, 0, 7]   #číslo 7014932
b = [8, 7, 6]               #číslo 678

if len(a) < len(b):
    a, b = b, a             #číslo "a" je delší

prenos = 0
c = []
for i in range(len(b)):
    x = a[i] + b[i] + prenos
    c.append(x%10)
    prenos = x // 10

for i in range(len(b), len(a)):
    x = a[i] + prenos
    c.append(x%10)
    prenos = x // 10
    
if prenos > 0:
    c.append(prenos)
    
print(c)                    #součet 7015610

