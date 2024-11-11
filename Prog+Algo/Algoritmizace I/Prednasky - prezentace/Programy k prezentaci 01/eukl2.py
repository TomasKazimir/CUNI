x = int(input("První číslo: "))
y = int(input("Druhé číslo: "))
while y > 0:
    x, y = y, x % y
print("NSD: ", x)
