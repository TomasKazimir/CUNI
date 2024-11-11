A = [[0] * 3 for i in range(3)]

B = [[0] * 3] * 3

print("A:", *A, sep="\n")
print("B:", *B, sep="\n")

A[0][0] = 1
B[0][0] = 1

print("A po zmene:", *A, sep="\n")
print("B po zmene:", *B, sep="\n")

