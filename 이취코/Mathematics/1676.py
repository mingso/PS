import sys

n = int(sys.stdin.readline())
ans = 1

for i in range(1, n+1):
    ans *= i

ans = str(ans)
striped = ans.rstrip('0')

print(len(ans) - len(striped))