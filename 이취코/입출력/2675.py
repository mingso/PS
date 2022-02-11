import sys

t = int(sys.stdin.readline())
for i in range(t):
    r, s = sys.stdin.readline().split()
    for w in s:
        for _ in range(int(r)):
            print(w, end="")
    print("")