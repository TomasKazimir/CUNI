c = 500

A = 0
B = 0
C = 0
AnB = 0
AnC = 0
BnC = 0
AnBnC = 0

for i in range(1, 501):
    if i % 8 == 0:
        A += 1
    if i % 12 == 0:
        B += 1
    if i % 15 == 0:
        C += 1
    if i % 8 == 0 and i % 12 == 0:
        AnB += 1
    if i % 8 == 0 and i % 15 == 0:
        AnC += 1
    if i % 12 == 0 and i % 15 == 0:
        BnC += 1
    if i % 8 == 0 and i % 12 == 0 and i % 15 == 0:
        AnBnC += 1
print(f"{A=}, {B=}, {C=}")
print(f"{AnB=}, {AnC=}, {BnC=}")
print(f"{AnBnC=}")
print(f"{500 - (A + B + C - AnB - AnC - BnC + AnBnC) = }")
