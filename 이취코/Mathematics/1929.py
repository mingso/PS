import sys

def isPrime(x):
    if x == 0 or x == 1:
        return False

    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

start, end = map(int, sys.stdin.readline().split())

for num in range(start, end+1):
    if isPrime(num):
        print(num)
