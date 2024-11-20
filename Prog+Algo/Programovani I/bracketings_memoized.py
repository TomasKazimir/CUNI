def memoized_bracketings_rec(n, stored, opened=0, closed=0):
    if opened + closed == 2 * n:
        return 1

    # lookup count in stored
    if (opened, closed) in stored:
        return stored[(opened, closed)]

    count = 0

    if opened < n:  # new opening bracket is possible
        count += memoized_bracketings_rec(n, stored, opened + 1, closed)

    if closed < opened:  # closing bracket is possible
        count += memoized_bracketings_rec(n, stored, opened, closed + 1)

    # store count
    stored[(opened, closed)] = count
    return count


print(memoized_bracketings_rec(int(input()), {}))