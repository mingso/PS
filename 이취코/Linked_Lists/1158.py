import sys

n, k = map(int, sys.stdin.readline().split())
people = [i for i in range(1, n+1)]

answer = []
num = 0

for i in range(n-1):
    num += (k - 1)
    if num >= len(people): # 한 바퀴 돌았을 때 바꿈
        num %= len(people)
    answer.append(people.pop(num))
answer.append(people.pop())

print("<" + ", ".join(map(str, answer)) + ">")
