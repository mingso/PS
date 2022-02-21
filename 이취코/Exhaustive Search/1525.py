import sys
E, S, M = map(int, sys.stdin.readline().split())
e, s, m = 1, 1, 1
answer = 1

while (E, S, M) != (e, s, m):
    e = (e + 1) % 15
    if e == 0:
        e = 15
    s = (s + 1) % 28
    if s == 0:
        s = 28
    m = (m + 1) % 19
    if m == 0:
        m = 19
    answer += 1

print(answer)