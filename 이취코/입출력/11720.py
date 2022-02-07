import sys

n = int(sys.stdin.readline())
numbers = sys.stdin.readline().rstrip()

li = list(map(int, numbers))
print(sum(li))