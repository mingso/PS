n, l, r = map(int, input().split())

data = []

for _ in range(n):
    data.append(list(map(int, input().split())))


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

answer = 0
for i in range(n):
    for j in range(n):
        for k in range(4):
            nx = i + dx[k]
            ny = i + dy[k]

            if nx < n and nx >= 0 and ny < n and ny >=0 :
                if l <= data[i][j] - data[nx][ny] <= r:
                    print("zw")
