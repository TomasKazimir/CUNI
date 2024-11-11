# Eratosthenovo síto

n = int(input("Horní mez prvočísel: "))
sito = [False, False] + [True] * (n-1)

i = 2
while i <= n:
    if sito[i]:                 # číslo "i" je prvočíslo
        j = 2 * i               # první násobek čísla "i"
        while j <= n:
            sito[j] = False     # násobek čísla "i" není prvočíslo
            j += i              # další násobek
    i = i + 1                   # další zkoumané číslo

for i in range (n+1):
    if sito[i]:
        print(i)
