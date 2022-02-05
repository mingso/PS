bi = "01001111"

pre = bi[:4]
post = bi[4:]

ind = [8, 4, 2, 1]
hexa = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']

hexa.index
sum1, sum2 = 0, 0
for i, n in enumerate(ind):
    sum1 += int(pre[i]) * n
    sum2 += int(post[i]) * n

HEX = str(hexa[sum1]) + str(hexa[sum2])
print(HEX)

dec = 13
ans = ""
while dec > 1:
    ans = str(dec % 2) + ans
    dec //= 2
ans = "1" + ans
print(dec, ans)

# binary to dic
