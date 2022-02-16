import sys

_, _ = map(int, sys.stdin.readline().split())

n = list(map(int, sys.stdin.readline().split()))
m = list(map(int, sys.stdin.readline().split()))

answer = n+m
answer.sort()
print(' '.join(map(str, answer)))