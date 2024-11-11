vstup = input()
list = vstup.split()
list.pop()
integers = [int(n) for n in list]
najvacsie = integers[0]
druhe = min(integers)

for i in integers:
    if i >= najvacsie:
        najvacsie = i

for i in integers:
    if i < najvacsie:
        if i >= druhe:
            druhe = i
    

# zoznam = [x for x in integers if x!=najvacsie]
# druhe = zoznam[0]
# for j in zoznam:
#     if j >= druhe:
#         druhe = j
# print(zoznam)

print(druhe)