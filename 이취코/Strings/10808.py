import sys

atoz = "abcdefghijklmnopqrstuvwxyz"
alphabet = {}

for alpha in atoz:
    alphabet[alpha] = 0

s = sys.stdin.readline().rstrip()

for a in s:
    alphabet[a] += 1

print(" ".join(map(str, alphabet.values())))