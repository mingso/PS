n = int(input())

data = []

student = []
teacher = []

answer = 'YES'
for _ in range(n):
    data.append(list(input().split()))
    for i, info in enumerate(data[_]):
        if info == 'S':
            student.append((_, i))

            # 일단 ST 바로 옆에 붙어있으면 안됨
            if (i + 1 < n and data[_][i + 1] == 'T') or (i > 0 and data[_][i - 1] == 'T') \
                    or (_ > 0 and data[_ - 1][i] == 'T'):
                answer = 'NO'
        elif info == 'T':
            teacher.append((_, i))

if answer == 'YES':
    obtacle = [[] for _ in range(len(teacher))]
    # 장애물 설치 할 수 있는 자리 구함
    for sx, sy in student:
        for i, (tx, ty) in enumerate(teacher):
            if sx == tx:
                if sy < ty:
                    for y in range(sy + 1, ty):
                        obtacle[i].append((sx, y))
                else:
                    for y in range(ty + 1, sy):
                        obtacle[i].append((sx, y))

            if sy == ty:
                if sx < tx:
                    for x in range(sx + 1, tx):
                        obtacle[i].append((x, sy))
                else:
                    for x in range(tx + 1, sx):
                        obtacle[i].append((x, sy))

    obtacle_ = sum(obtacle, [])
    count = {}
    for i in obtacle_:
        try:
            count[i] += 1
        except:
            count[i] = 1

    def f(x):
        return x[1]

    # 겹치는게 있으면 삭제
    count = sorted(count.items(), key=f, reverse=True)

    obt = 3
    for key, value in count:
        if value > 1:
            flag = 0
            for i, item in enumerate(obtacle):
                if item.count(key) >= 1:
                    obtacle[i].clear()
                    flag = 1
            if flag == 1:
                obt -= 1

    if(len(obtacle)-obtacle.count([]) > obt):
        answer = "NO"

print(answer)
