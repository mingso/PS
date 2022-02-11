import sys

def isPrime(x):
    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    for x in range(3, int(n/2) + 1, 2):
        if isPrime(x) and isPrime(n - x):
            print("%d = %d + %d" % (n, x, n - x))
            break