import sys
sys.setrecursionlimit(10**6)

cache = {}


def fib(n):
    if n in cache:
        return cache[n]
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fib(n - 1) + fib(n - 2)
    cache[n] = value
    return value


ai = (f(i) % 2021)+(i % 50)

N = int(input())
for i in range(N):
    rep =
