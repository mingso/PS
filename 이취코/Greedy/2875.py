import sys

w, m, k = map(int, sys.stdin.readline().split())

wt = w // 2
wr = w % 2

while k > 0:
    if wt > m:
        wt -= 1
        k -= 2
    elif m >= wt:
        m -= 1
        k -=1

if wt == m:
    print(m)
elif wt > m:
    print(m)
elif m > wt :
    print(wt)