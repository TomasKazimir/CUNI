def convert_num_from_b1_to_b2(n: str, b1: int, b2: int) -> str:
    numerals = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if b1 == 10:
        x = int(n)
    else:
        x = 0
        for i in n:  # horner
            x = x*b1 + int(numerals.index(i))

    if b2 == 10:
        return str(x)
    
    out = ""
    while x > 0:  # reverse
        out = numerals[x % b2] + out
        x //= b2
    
    return out


#  INPUT: AFG1A 18 1554559F 22 8
# OUTPUT: 27010155325
#
# input a number and its base, another number and its base and desired output base of their sum

n1, b1, n2, b2, b3 = input().split()
b1, b2, b3 = int(b1), int(b2), int(b3)

n1 = int(convert_num_from_b1_to_b2(n1, b1, 10))
n2 = int(convert_num_from_b1_to_b2(n2, b2, 10))
n3 = convert_num_from_b1_to_b2(str(n1 + n2), 10, b3)
print(n3)