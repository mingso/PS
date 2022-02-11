import sys

def minus(a, b):
    return a - b

a, b = map(int, sys.stdin.readline().split())
sys.stdout.write(str(minus(a, b)))