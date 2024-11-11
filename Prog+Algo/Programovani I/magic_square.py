def is_magic(sq: list):
    s = sum(sq[0])
    n = len(sq)

    # rows
    for i in sq[1:]:
        if sum(i) != s:
            return False
    
    # columns
    for j in range(n):
        if sum([i[j] for i in sq]) != s:
            return False
    
    # diagonal 1
    if sum([row[i] for i, row in enumerate(sq)]) != s:
        return False
    
    # diagonal 2
    if sum([row[i] for i, row in enumerate(reversed(sq))]) != s:
        return False
    
    return True


square = []
row = [int(x) for x in input().split()]
for _ in range(len(row) - 1):
    square.append(row)
    row = [int(x) for x in input().split()]
square.append(row)
n = len(square)


for i in range(n):
    for j in range(n):
        if square[i][j] == 0:
            break
    else: continue
    break


base_sum = sum(square[0]) if i != 0 else sum(square[1])
square[i][j] = base_sum - sum(square[i])

if is_magic(square):
    for row in square:
        print(*row)
else:
    print("Can't be magic")
