n = int(input())
k = int(input())

_map = [[0] * (n+1)] * (n+1)

for _ in range(k):
    x, y = map(int, input().split())
    _map[x][y] = 1

# 0은 빈공간, 1은 사과

l = int(input())
direction = []
for _ in range(l):
    x, c = input().split()
    direction.append((int(x), c))

direction.append((0, 0))

dir = [(0,1), (1, 0), (0, -1), (-1, 0)]
direc = 0
length = 1
body = [(1, 1)]
d = 0

time = 0
while True:
    if direction[d][0] == time:
        if direction[d][1] == 'D':
            direc += 1
            direc %= 4
        else :
            direc -= 1
            if direc == -1:
                direc = 3
        d += 1

    y = body[0][0] + dir[direc][0]
    x = body[0][1] + dir[direc][1]
    if (x < 1) or (x > n) or (y < 1) or (y > n) :
        break

    body.insert(0, (y, x))
    print(body[0][0], body[0][1])
    if _map[body[0][0]][body[0][1]] != 1:
        body.pop()
    else :
        _map[body[0][0]][body[0][1]] = 0

    time += 1

    print(body)

print(time+1)