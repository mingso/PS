n = int(input())
data = []

for _ in range(n):
    t, p = map(int, input().split())
    data.append((t, p))

next_day = 0
pay = 0
# 1 시작
for i, (t, p) in enumerate(data):
    if t + i <= n :
        if i >= next_day:
            pay += p
            data[i] = (t, pay)
            next_day += t
    else :
        data[i] = (t, 0)

print(data)