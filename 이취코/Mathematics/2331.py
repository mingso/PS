import sys
import math

a, p = sys.stdin.readline().split()
p = int(p)

d = [int(a)]
dup = 0

while True:
    res = 0
    for i in str(d[-1]):
        res += math.pow(int(i), p)

    if res == dup:
        break
    elif res in d:
        dup = res
    else:
        d.append(int(res))

print(len(d[:d.index(dup)]))
