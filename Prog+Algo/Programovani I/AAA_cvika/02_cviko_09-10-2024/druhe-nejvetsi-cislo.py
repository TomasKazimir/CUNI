"""
V seznamu celých čísel ukončeném -1, které nepatří do seznamu, nalezněte a vypište druhou největší hodnotu. Seznam má vždy alespoň dvě různé hodnoty a čísla se v něm mohou opakovat, každé číslo je zapsané na samostatném řádku.

Např. je-li na vstupu posloupnost

4
5 
1 
4 
5 
3
-1 

bude výstupem číslo
4

Není povoleno ukládat si v programu zadanou posloupnost čísel do pole nebo seznamu.
"""

n = int(input())
nejvetsi = n
druhe_nejvetsi = None

while n != -1:
    if n > nejvetsi:
        druhe_nejvetsi = nejvetsi
        nejvetsi = n
    elif nejvetsi > n:
        if druhe_nejvetsi == None:
            druhe_nejvetsi = n
        elif n > druhe_nejvetsi:
            druhe_nejvetsi = n
    n = int(input())

if druhe_nejvetsi != nejvetsi and druhe_nejvetsi != None:
    print(druhe_nejvetsi)
