import sys

def isPrime(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

n = int(sys.stdin.readline())
half = int(n/2) + 1

while n > 1:
    if isPrime(n):
        print(int(n))
        n = 1
        break

    for i in range(2, half):
        if n % i == 0:
            print(i)
            n /= i
            break