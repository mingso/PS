import sys

def quad(x, y, n):
    global answer

    now = video[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if video[i][j] != now:
                answer += '('
                for k in range(2):
                    for l in range(2):
                        quad(x + k * n//2, y + l * n//2, n//2)
                answer += ')'
                return

    if now == 0:
        answer += '0'

    elif now == 1:
        answer += '1'

answer = ""
n = int(sys.stdin.readline())
video = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

quad(0, 0, n)

print(answer)