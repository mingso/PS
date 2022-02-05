n = int(input())

li = []

for i in range(n):
    m = int(input())

    if len(li) == 0:
        li.append(m)

    else :
        num = 0
        for j in range(0, len(li)):
            if m > li[j] :
                break
            else :
                num += 1

        li.insert(num, m)

print(li)