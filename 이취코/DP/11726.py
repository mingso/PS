import sys

n = int(sys.stdin.readline())
d = [0, 1, 2]
for i in range(3, n+1):
    d.append(d[i - 1] + d[i - 2])

sys.stdout.write(str(d[n] % 10007))