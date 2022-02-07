import sys

def add(a, b):
    return a + b

a, b = map(int, sys.stdin.readline().split())
sys.stdout.write(str(add(a, b)))