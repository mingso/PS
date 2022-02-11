import sys

t = int(sys.stdin.readline())

for i in range(t) :
    score = 0
    res = sys.stdin.readline()
    con = 0
    for r in res:
        if r == "O":
            con += 1
            score += con
        else:
            con = 0
    print(score)
