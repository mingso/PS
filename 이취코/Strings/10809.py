import sys

atoz = "abcdefghijklmnopqrstuvwxyz"
alphabet = {}

for alpha in atoz:
    alphabet[alpha] = -1

sen = sys.stdin.readline().rstrip()

for i in range(len(sen)):
    if alphabet[sen[i]] == -1:
        alphabet[sen[i]] = i

print(" ".join(map(str, alphabet.values())))