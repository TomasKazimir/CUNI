a = [28, 16, 1, 43, 16, 7, 20, 18, 35]

def trid_vkladanim(a):
    for i in range(1, len(a)):   # vkládáme číslo z pozice "i"
        x = a[i]
        j = i-1
        while j >= 0 and x < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = x

trid_vkladanim(a)
print(a)

        
