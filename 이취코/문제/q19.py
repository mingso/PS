n = int(input())
num = list(map(int, input().split()))

op = list(map(int, input().split()))

max_value = -1e9
min_value = 1e9

def cal(i, now):
    global max_value, min_value, op

    if i == n :
        min_value = min(min_value, now)
        max_value = max(max_value, now)

    else :
        if op[0] > 0 :
            op[0] -= 1
            cal(i+1, now + num[i])
            op[0] += 1
        if op[1] > 0:
            op[1] -= 1
            cal(i+1, now - num[i])
            op[1] += 1
        if op[2] > 0:
            op[2] -= 1
            cal(i+1, now * num[i])
            op[2] += 1
        if op[3] > 0:
            op[3] -= 1
            cal(i+1, int(now / num[i]))
            op[3] += 1

cal(1, num[0])

print(max_value)
print(min_value)