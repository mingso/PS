import sys
from itertools import combinations

l, _ = map(int, sys.stdin.readline().split())
alphabets = list(map(str,  sys.stdin.readline().split()))
alphabets.sort()
vowel = ['a', 'e', 'i', 'o', 'u']

result = list(combinations(alphabets, l))
answer = []
for res in result:
    num_vowel = 0
    num_consonant = 0
    for r in res:
        if r in vowel:
            num_vowel += 1
        else:
            num_consonant += 1
    if num_vowel >= 1 and num_consonant >= 2:
        answer.append(''.join(map(str, res)))

for a in answer:
    print(a)
