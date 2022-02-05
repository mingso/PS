t = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


for _ in range(t):
    n = int(input())
    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))

    dist = [[1e9] * n for i in range(n)]
    dist[0][0] = data[0][0]

    for i in range(n):
        for j in range(n):
            for a in range(4):
                nx = dx[a]
                ny = dy[a]
                if i + nx >= 0 and j + ny >= 0 and i + nx < n and j + ny < n :
                    dist[i + nx][j+ ny] = min(dist[i+nx][j+ny], data[i+nx][j+ny] + dist[i][j])

    for i in reversed(range(n)):
        for j in reversed(range(n)):
            for a in range(4):
                nx = dx[a]
                ny = dy[a]
                if i + nx >= 0 and j + ny >= 0 and i + nx < n and j + ny < n:
                    dist[i + nx][j + ny] = min(dist[i + nx][j + ny], data[i + nx][j + ny] + dist[i][j])

    for i in range(n):
        for j in range(n):
            for a in range(4):
                nx = dx[a]
                ny = dy[a]
                if i + nx >= 0 and j + ny >= 0 and i + nx < n and j + ny < n :
                    dist[i + nx][j+ ny] = min(dist[i+nx][j+ny], data[i+nx][j+ny] + dist[i][j])

    print(dist[n-1][n-1])