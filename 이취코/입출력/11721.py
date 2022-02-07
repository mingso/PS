import sys

line = sys.stdin.readline()

for i, a in enumerate(line):
    sys.stdout.write(a)
    if (i + 1) % 10 == 0:
        sys.stdout.write("\n")
