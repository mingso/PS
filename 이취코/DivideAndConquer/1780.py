import sys

def clipPaper(x, y, n):
    global answerM1, answer0, answer1
    now = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != now:
                for k in range(3):
                    for l in range(3):
                        clipPaper(x + k * n//3, y + l * n//3, n//3)
                return

    if now == -1:
        answerM1 += 1
    elif now == 0:
        answer0 += 1
    elif now == 1:
        answer1 += 1

n = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

answerM1= 0
answer0 = 0
answer1 = 0

clipPaper(0, 0, n)

print(answerM1)
print(answer0)
print(answer1)
