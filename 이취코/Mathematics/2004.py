import sys

def countTwo(x):
    res = 0
    while x != 0:
        x = x // 2
        res += x
    return res

def countFive(x):
    res = 0
    while x != 0:
        x = x // 5
        res += x
    return res

n, m = map(int, sys.stdin.readline().split())

print(min(countTwo(n) - countTwo(n - m) - countTwo(m), countFive(n) - countFive(n - m) - countFive(m)))