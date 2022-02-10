import sys

s = sys.stdin.readline().rstrip()
jubmisa = []

for i in range(len(s)):
    jubmisa.append(s[i:])

jubmisa.sort()
print("\n".join(map(str, jubmisa)))