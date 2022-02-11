import sys

max = 0
index = -1
for i in range(9):
    n = int(sys.stdin.readline())
    if max < n:
        max = n
        index = i + 1

print(max)
print(index)