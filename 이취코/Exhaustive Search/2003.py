import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

answer = 0
for i in range(n):
    for j in range(i+1, n+1):
        if sum(arr[i:j]) == m:
            answer += 1

print(answer)