matrix = []
row = [int(x) for x in input().split()]
for _ in range(len(row) - 1):
    matrix.append(row)
    row = [int(x) for x in input().split()]
matrix.append(row)
n = len(matrix)

out = [1, 1, 1]

# hlavni diagonala
for i in range(n):
    for j in range(i, n):
        if matrix[i][j] != matrix[j][i]:
            out[0] = 0
            break
    else: continue
    break

# vedlejsi diagonala
for i in range(n):
    for j in range(i, n):
        if matrix[i][-1-j] != matrix[j][-1-i]:
            out[1] = 0
            break
    else: continue
    break

# svisla osa
for i in range(n):
    for j in range(n // 2):
        if matrix[i][j] != matrix[i][-1-j]:
            out[2] = 0
            break
    else: continue
    break

print(*out)