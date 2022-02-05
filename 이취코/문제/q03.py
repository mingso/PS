s = input()

count = 0
for n, i in enumerate(s):
    if n > 0 and i != s[n-1] :
        count += 1

print(int(count/2))