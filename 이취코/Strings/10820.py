import sys

while True:
    sen = sys.stdin.readline()
    if sen == "":
        break
    lo, up, num, space = 0, 0, 0, 0
    for s in sen:
        if s.islower():
            lo += 1
        elif s.isupper():
            up += 1
        elif s.isnumeric():
            num += 1
        elif s.isspace():
            space += 1
    print(lo, up, num, space-1)