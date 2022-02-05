n = int(input())

subject = []

for i in range(1, n+1):
    a = list(map(int, input().split()))
    t = a[0]
    pre = a[1: len(a)-1]

    subject.append([i, t])
    time = 0
    for p in pre:
        if time < subject[p-1][1]:
            time = subject[p-1][1]
    t += time

    subject[i-1] = (i, t)

    print(t)