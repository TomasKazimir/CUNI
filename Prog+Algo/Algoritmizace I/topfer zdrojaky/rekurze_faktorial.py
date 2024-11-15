def factorial(n):
    f = 1
    for i in range(2, n+1):
        f *= i
    return f


def factorial_recursion(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))