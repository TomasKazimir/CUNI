a = [28, 16, 1, 43, 16, 7, 20, 18, 35]
#a = [5, 4, 3, 2, 1]

def trid_bublinkove(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

trid_bublinkove(a)
print(a)

