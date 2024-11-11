import random 

# generace seznamu
N = 100
M = 50

numlst = [] 
 
while len(numlst) < N + M: 
    rnd = random.randint(0, 1_000_000_000) 
    if rnd in numlst: 
        continue 
    numlst += [rnd] 

list_x = sorted(numlst[0:N])
list_y = sorted(numlst[N:])

# print("LIST X")
# for x in list_x: 
#     print(x)
# print("LIST Y")
# for y in list_y: 
#     print(y)
# print("---------------")

# konec generace seznamu

print("zacatek algoritmu....")

# list_x = seznam s prvky x1 az xn
# list_y = seznam s prvky y1 az yn



result = []  # vysledny serazeny seznam co vratim

i, j = 0, 0
while i < len(list_x):
    if j == len(list_y):  # zatridil jsem vsechny prvky ze seznamu y
        result += list_x[i:]
        break
    if list_x[i] < list_y[j]:     # pokud podminka
        result.append(list_x[i])  # tak zatridim prvek z list_x
        i += 1                    # a posouvam se v tomto seznamu dal
    else:                         # jinak 
        result.append(list_y[j])  # zatridim prvek z list_y 
        j += 1                    # a posouvam se v tomto seznamu indexem dal
if len(result) < len(list_x) + len(list_y):  # jsem na konci list_x a nejake prvky v list_y mi jeste zbyly
    result += list_y[j:]                     # tak ten konec list_y prilepim nakonec resultu

print("konec algoritmu....")

# dale uz jen porovnavani vystupu se serazenymi seznamy a kontrola spravnosti

print(sorted(list_x + list_y))
print(result)

print("result \t\t co by to melo byt")
for i in range(len(list_x + list_y)):
    a, b = result[i], sorted(list_x + list_y)[i]
    print(a, b, sep="\t\t")
    if a != b:
        print("CHYBA VOLE NEFUNGUJE TO")