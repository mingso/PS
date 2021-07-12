g = int(input())
p = int(input())
gi = [0] * g

data = []
for _ in range(p):
    data.append(int(input()))

answer = 0
for i in data:
    n = gi.count(1)
    if n < g:
        for j in range(i-1, -1, -1):
            if gi[j] == 0:
                gi[j] = 1
                answer +=1
                break
    else :
        break

    if n == gi.count(1):
        break

print(answer)