import sys

atoz = "abcdefghijklmnopqrstuvwxyz"
sen = sys.stdin.readline().rstrip()
answer = ""
for s in sen:
    i = atoz.find(s.lower())
    if i == -1:
        answer += s
        continue
    if s.isupper():
        answer += atoz[(i + 13) % 26].upper()
    else:
        answer += atoz[(i + 13) % 26]

print(answer)