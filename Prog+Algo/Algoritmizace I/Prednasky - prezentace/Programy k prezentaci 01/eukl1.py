x = int(input("První číslo: "))
y = int(input("Druhé číslo: "))
while x != y:
    if x > y:
        x -= y
    else:
        y -= x
print("NSD: ", x)

