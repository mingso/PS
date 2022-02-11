import sys
import math

a, b = map(int, sys.stdin.readline().split())

m = int(sys.stdin.readline())
aa = list(map(int, sys.stdin.readline().split()))

answer = []
num = 0

for i in range(len(aa)):
    num += aa[i] * math.pow(a, len(aa) -1 - i)
num = int(num)

while num >= b:
    answer.append(num % b)
    num //= b

answer.append(num)

print(' '.join(map(str, reversed(answer))))