from itertools import combinations

n, m = map(int, input().split())

Map, chicken = [], []

for _ in range(n):
    Map.append(list(map(int, input().split())))
    num = Map[_].count(2)
    if num == 1 :
        chicken.append((_, Map[_].index(2)))
    elif num >= 2:
        for i in range(n):
            if Map[_][i] == 2:
                chicken.append((_, i))

candidates = list(combinations(chicken, m))

chicken_length = [[] for _ in range(len(chicken))]


for i in range (len(chicken)):
    for a in range(n):
        for b in range(n):
            if Map[a][b] == 1 :
                x = abs(chicken[i][0] - a)
                y = abs(chicken[i][1] - b)
                chicken_length[i].append(x+y)

#
# if len(chicken_length[0]) > m :
#     for i in range (len(chicken_length[0]) - m) :
#         # 1, 2, 3의 거리가 가장 적은거 삭제

chicken_length.pop(1)

ans = 0
for i in range(len(chicken_length[0])):
    tmp = 100
    for j in range(len(chicken_length) - 1):
        print(chicken_length[j][i])
        tmp = min(tmp, chicken_length[j][i], chicken_length[j+1][i])
    ans += tmp
print(ans)