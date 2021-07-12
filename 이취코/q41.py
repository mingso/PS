n, m = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

for i, info in enumerate(data):
    for j, inf in enumerate(info):
        if inf == 1:
            for o, inff in enumerate(data[j]):
                if inff == 1:
                    data[i][o] = 1

route = list(map(int, input().split()))

answer = 'YES'
for r in range(m-1):
    if data[route[r]][route[r+1]] != 1:
        answer = 'NO'
        break

print(answer)