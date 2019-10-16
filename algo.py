# Uses python3

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current % 10, (previous + current) % 10

    return current % 10


def fib(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for i in range(n - 1):
        previous, current = current, previous + current

    return current


def gcd(a, b):
    if b == 0:
        return a
    if a % b == 0:
        return b
    a, b = b, a % b
    return gcd(a, b)


def fibonacci_huge(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    if m == 2:
        return fib(n % 3) % m
    if m == 3:
        return fib(n % 8) % m
    else:
        for _ in range(n - 1):
            previous, current = current % m, (previous + current) % m

        return current % m

# a, b = map(int, input().split())
# print(fibonacci_huge(a, b))
