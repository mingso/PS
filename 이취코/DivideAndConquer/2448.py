import sys

def staring(m):
    global map

    if m == 3:
        map[0][n - 3:n + 2] = [0, 0, 1, 0, 0]
        map[1][n - 3:n + 2] = [0, 1, 0, 1, 0]
        map[2][n - 3:n + 2] = [1, 1, 1, 1, 1]
        return

    a = m // 2
    staring(a)

    for i in range(a):
        map[a+i][n - (a*2):n - a] = map[i][n - a:n + a - 1]
        map[a+i][n: n + (a*2 + 1)] = map[i][n - a:n - 1 + a]


n = int(sys.stdin.readline())

map = [[0 for i in range(n*2 - 1)] for j in range(n)]
staring(n)

for i in map:
    for j in i:
        if j:
            print('*', end='')
        else:
            print(' ', end='')
    print()