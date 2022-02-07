import sys

num = int(sys.stdin.readline())

for i in range(1, 10):
    print("%d * %d = %d" % (num, i, num*i))