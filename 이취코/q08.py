s = list(map(str, input()))

s.sort()

num = 0
ans = []
for item in s :
    if item.isdigit() :
       num += int(item)
    else :
        ans.append(item)

ans.append(num)

for _ in ans:
    print(_, end='')