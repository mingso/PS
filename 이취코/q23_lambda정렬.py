n = int(input())

data = []
for _ in range(n):
    data.append(list(input().split()))

# 국어 내림차순 (data[][1])
# 영어 오름차순 (data[][2])
# 수학 내림차순 (data[][3])
# 이름 알파벳순 (data[][0])

data.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for d in data:
    print(d[0])


