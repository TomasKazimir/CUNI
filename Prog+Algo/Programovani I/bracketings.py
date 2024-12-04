def bracketings(n, opened=0, closed=0):
    if opened + closed == 2 * n:
        return 1
    count = 0
    if opened < n:  # new opening bracket is possible
        count += bracketings(n, opened + 1, closed)
    if closed < opened:  # closing bracket is possible
        count += bracketings(n, opened, closed + 1)
    return count
print(bracketings(int(input())))