import sys

def cal(s, g):
    answer = 0

    if g - s > 0:
        if u == 0:
            return -1

        retains = g - s

        answer += retains // u
        retains %= u
        s += answer * u

        if retains == 0:
            return answer

        while (g-s) % u != 0:
            s -= d
            answer += 1

            if s < 1:
                return -1

        answer += (g-s) // u
        return answer

    elif g - s < 0:
        retains = abs(g - s)
        if d == 0:
            return -1

        answer += retains // d
        retains %= d
        s -= answer * d

        if retains == 0:
            return answer

        while abs(g-s) % d != 0:
            s += u
            answer += 1

            if s > f:
                return -1

        answer += abs(g-s) // d
        return answer

    return answer

f, s, g, u, d = map(int, sys.stdin.readline().split())

answer = cal(s, g)

print(answer if answer != -1 else "use the stairs")