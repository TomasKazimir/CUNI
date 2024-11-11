a = [28, 16, 1, 43, 16, 7, 20, 18, 35]

def trid_vyberem(a):
    for i in range(len(a)-1):   # umístit číslo na pozici "i"
        k = i
        for j in range(i+1, len(a)):
            if a[j] < a[k]:
                k = j
        if k > i:
            a[k], a[i] = a[i], a[k]

trid_vyberem(a)
print(a)

        
