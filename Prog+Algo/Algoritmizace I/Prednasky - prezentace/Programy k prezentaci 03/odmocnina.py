def odmocnina(n):
    eps = 0.0001
    if n > 1:
        dolni, horni = 1, n
    else:
        dolni, horni = 0, 1
    stred = (dolni + horni)/2
    while horni - dolni >= eps:
        if stred**2 < n:
            dolni = stred
        else:
            horni = stred
        stred = (dolni + horni)/2
        print(stred)
    return stred

print(f"{odmocnina(90000): 0.3f}")
