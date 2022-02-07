import sys

n = int(sys.stdin.readline())
d = [0, 1, 3]
for i in range(3, n+1):
    a = d[i - 1] * 2
    if i % 2 == 0:
        a += 1
    else:
        a -= 1
    d.append(a)

sys.stdout.write(str(d[n] % 10007))