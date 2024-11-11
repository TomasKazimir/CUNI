def strom(K, L):
    for i in range(K):
        print("." * (K - i - 1) + "*" * (2*i + 1) + "." * (K-i-1))
    for i in range(L):
        print("." * (K-1) + "*" + "." * (K-1))

strom(int(input()), int(input()))

