def vytvor_matici_stromu(K, L):
    out = []
    for i in range(K):
        out.append([0] * (K - i - 1) + [1] * (2*i + 1) + [0] * (K-i-1))
    for i in range(L):
        out.append([0] * (K-1) + [1] + [0] * (K-1))
    return out

def preved_matici_na_text(matice):
    return "\n".join(["".join(["  " if char == 0 else " *" for char in radek]) for radek in matice])

def main():
    stromecky = []
    M, N = 0, 0
    while (line := input()) != "":
        line = tuple(int(x) for x in line.split())
        stromecky.append(line)
        M = max(M, line[1] + line[2] + line[3])
        N = max(N, line[0] + 2 * line[2] - 1)

    matice_lesa = [[0] * N for _ in range(M)]

    print(f"Rozmery lesa: {M = }, {N = }")
    print("Jednotlive stromecky:")

    for strom in stromecky:
        x, y, k, l = strom
        matice_stromu = vytvor_matici_stromu(k, l)
        print(strom, preved_matici_na_text(matice_stromu), sep="\n", end="\n~~~~~~~~~~~~~~~~~~~~~~~\n")
        for i in range(y, y + k + l):
            for j in range(x, x + 2 * k - 1):
                matice_lesa[i][j] += matice_stromu[i - y][j - x]

    print("Les:")
    print(preved_matici_na_text(matice_lesa), sep="\n")

if __name__ == "__main__":
    main()
                
