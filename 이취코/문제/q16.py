n, m = map(int, input().split())
data = []
virus = []
tmp = [[0] * m for _ in range(n)]

for _ in range(n):
    data.append(list(map(int, input().split())))

    # 일단 virus의 위치를 찾자.
    if data[_].count(2) != 0 :
        for i, num in enumerate(data[_]):
            if num == 2:
                virus.append((_, i))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

def spread(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m :
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                spread(nx, ny)

def count0():
    cnt = 0

    for i in tmp:
        cnt += i.count(0)

    return cnt

def dfs(count):
    global result

    if count == 3:
        for i in range(n):
            print(tmp[i])
            for j in range(m):
                tmp[i][j] = data[i][j]
                print(data[i][j], end = ' ')

        for (x, y) in virus:
            spread(x, y)

        result = max(result, count0())
        return

    # 모든 경우의 수 계산
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)