for n in range(127, 128):
    n=30
    puvodni_n = int(n)
    c = 0
    while n > 0:
        if n % 2 == 1:
            print("-1")
            c += 1
            n = n - 1
        else:
            print("//2")
            c += 1
            n = n // 2
    print(f"pocet hvezd pro n = {puvodni_n} je {c}")
    break
