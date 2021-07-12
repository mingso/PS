n, k = map(int, input().split())

virus_list = [0] * (k+1)
virus_list[0] = 1
data = []
isVisited = [[0] * n for _ in range(n)]

for _ in range(n):
    data.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

x = x-1
y = y-1

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def virus_order(d):
    flag = 1
    for l in range(d):
        if virus_list[l] == 0:
            flag = 0
            break
    return flag

for _ in range(s):
    while virus_list.count(1) != k+1:
        for i in range(n):
            for j in range(n):
                if data[i][j] != 0 and isVisited[i][j] == 0 and virus_list[data[i][j]] == 0:
                    flag = virus_order(data[i][j])
                    if flag == 1:
                        for a in range(4):
                            nx = dx[a] + i
                            ny  = dy[a] + j
                            if nx >= 0 and nx < n and ny >= 0 and ny < n and data[nx][ny] == 0:
                                data[nx][ny] = data[i][j]
                        virus_list[data[i][j]] = 1
                        isVisited[i][j] = 1

    virus_list = [0] * (k + 1)
    virus_list[0] = 1

print(data[x][y])