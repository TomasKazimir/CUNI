matrix = []
m, n = (int(c) for c in input().split())
for _ in range(m):
    row = [int(x) for x in input().split()]
    matrix.append(row)
minimum = min([min(row) for row in matrix])
matrix = [[x - minimum for x in row] for row in matrix]
print(*[row for row in matrix], sep="\n")