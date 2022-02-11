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

x, y = map(int, sys.stdin.readline().split())

print(gcd(x, y))
print(lcm(x, y))