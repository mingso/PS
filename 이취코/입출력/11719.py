import sys

sum = 0
while True:
    try:
        a = int(sys.stdin.readline())
        sum += a
    except EOFError:
        break
