import sys

def hanoi(n, start, to, via):
    if n == 1:
        move(start, to)
    else:
        hanoi(n-1, start, via, to)
        move(start, to)
        hanoi(n-1, via, to ,start)

def move(start, to):
    answer.append((start, to))

n = int(sys.stdin.readline())

answer = []

hanoi(n, 1, 3, 2)

print(len(answer))
for ans in answer:
    print(ans[0], ans[1])