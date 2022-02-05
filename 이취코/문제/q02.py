s = input()

res = 0
for num in s :
    num = int(num)
    if res == 0 or num == 0:
        res += num
    else :
        res *= num

print(res)