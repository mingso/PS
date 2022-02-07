import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    d = [0, 1, 2, 4]
    for i in range(4, n+1):
        a = d[i - 1] + d[i - 2] + d[i - 3]
        d.append(a)

    print(str(d[n] % 10007))