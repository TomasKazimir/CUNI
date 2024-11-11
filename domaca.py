seznam = [int(n) for n in input().split()[:-1]]
naj, druhe = seznam[0], min(seznam)

for i in seznam:
    if i > naj:
        druhe = naj
        naj = i
        continue
    if naj > i > druhe:
        druhe = i

print(druhe)
