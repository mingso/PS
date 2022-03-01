import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

answer = 0
for i in range(n):
    for j in range(i+1, n+1):
        s = sum(arr[i:j])
        if s == m:
            answer += 1
            break
        elif s > m:
            break

print(answer)