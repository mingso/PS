import sys

n = int(sys.stdin.readline())

for i in range(1, n):
    sys.stdout.write(' ' * (n-i))
    for j in range(i * 2 - 1):
        if j == 0 or j == i*2-2:
            sys.stdout.write('*')
        else:
            sys.stdout.write(' ')
    sys.stdout.write('\n')

print('*' * (n*2-1))
