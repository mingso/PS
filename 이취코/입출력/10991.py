import sys

n = int(sys.stdin.readline())

for i in range(1, n+1):
    sys.stdout.write(' ' * (n-i))
    for j in range(i * 2 - 1):
        if j % 2 == 0:
            sys.stdout.write('*')
        else:
            sys.stdout.write(' ')

    sys.stdout.write('\n')
