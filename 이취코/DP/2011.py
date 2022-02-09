import sys
n = sys.stdin.readline()

d = [0] * (len(n)+1)
d[0] = 1
d[1] = 2

for i in range(2, len(n)+1):
    d[i] = d[i-2] + d[i-1]

li = "1"

for i in range(1, len(n) - 1):
    if n[i] == "0":
        if int(n[i-1]) >= 3 or n[i-1] == "0":
            li += "3"
            break
        li += "1"

    elif 10 <= int(n[i-1:i+1]) <= 26 and n[i+1] != "0":
        li += "2"
    else:
        li += "1"

nums = li.split("1")
answer = 1

if li.find("3") != -1 or n[0] == "0":
    answer = 0

else:
    for i in nums:
        answer *= d[len(i)]

print(answer%1000000)