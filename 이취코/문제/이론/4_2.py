n = int(input())

# 03, 13, 23, 30~39, 43, 53초/분
# 3, 13, 23 시 -> 60*60 = 3600번

res = 0
for i in range(n + 1):
    if(i == 3 or i == 13 or i == 23):
        res += 60 * 60
    else :
        res += (60-15)*15 + 15*60

print(res)