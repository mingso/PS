import sys

n = int(sys.stdin.readline())

for i in range(1, n+1):
    for j in range(n):
        sys.stdout.write("*")
    sys.stdout.write('\n')