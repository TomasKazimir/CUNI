n = 0
c = 0
s = 0
while True:
    n = input()
    if n == ".":
        print(s/c)
        break
    n = int(n)
    c += 1
    s += n
    
    
