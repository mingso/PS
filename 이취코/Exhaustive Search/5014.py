import sys

f, s, g, u, d = map(int, sys.stdin.readline().split())

retains = g - s
answer = 0

if retains > 0:
    if retains < u:
        while retains % u != 0:
            retains += d
            answer += 1

            if retains > f:
                answer = 0
                break

    if retains % u == 0:
        answer += retains // u
    elif (retains % u) % d == 0:
        answer += retains // u
        answer += 1
        answer += (retains % u)//d

elif retains < 0:
    retains = abs(retains)

    if retains < d:
        while retains % d != 0:
            retains += u
            answer += 1

            if retains > f:
                answer = 0
                break

    try:
        if retains % d == 0:
            answer += retains // d
        elif (retains % d) % u == 0:
            answer += retains // d
            answer += 1
            answer += (retains % d)//u
    except:
        answer = 0

print(answer if answer != 0 else "use the stairs")