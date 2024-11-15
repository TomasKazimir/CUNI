from functools import cache


@cache
def fib_recursion(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_recursion(n-1) + fib_recursion(n-2)

def fib_dynamic_programming(n):
    if n == 0:
        return 0
    a = 0; b = 1
    while n > 1:
        a, b = b, a+b
        n -= 1
    return b

