def maximize_reward(k, p):
    total_opponents = p

    dp_table = [[100_000] * (total_opponents + 1) for _ in range(k + 1)]
    path = [[j for j in range(total_opponents + 1)] for _ in range(k + 1)]

    for j in range(1, total_opponents + 1):
        dp_table[1][j] = 100_000

    for i in range(2, k + 1):
        for j in range(1, total_opponents + 1):
            for v in range(1, j):
                reward = (100_000 * v) // j + dp_table[i - 1][j - v]
                if reward > dp_table[i][j]:
                    dp_table[i][j] = reward
                    path[i][j] = str(v) + " " + str(path[i - 1][j - v])

    print("=======" * total_opponents)
    for row in dp_table[1:]:
        print(*[str(x).rjust(6) for x in row[1:]])
    print("=======" * total_opponents)
    for row in path[1:]:
        print(*[str(x).rjust(k*2) for x in row[1:]])
    print("=======" * total_opponents)

    print(dp_table[k][total_opponents])
    print(path[k][total_opponents])


maximize_reward(int(input()), 100)
