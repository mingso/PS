import sys

def gcd(x, y): # 최대공약수
    if y == 0:
        return x
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)

def lcm(x, y): # 최소공배수
    return int((x * y) / gcd(x, y))

t = int(sys.stdin.readline())

for _ in range(t):
    x, y = map(int, sys.stdin.readline().split())
    print(lcm(x, y))