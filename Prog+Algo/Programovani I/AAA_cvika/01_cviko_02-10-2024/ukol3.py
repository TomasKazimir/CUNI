from math import log

while True:
    n = int(input())
    if n  2 == 0:
        print(n, " je mocnina dvou - 2^", int(log(n, 2)))
    else:
        print(n, " neni mocnina dvojky")
