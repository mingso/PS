import sys

def gcd(x, y):
    mod = x % y
    while mod > 0:
        x = y
        y = mod
        mod = x % y
    return y

x, y = map(int, sys.stdin.readline().split())
print('1' * gcd(x, y))