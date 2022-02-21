import sys

n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]
minus = []
nums.sort(reverse=True)
answer = 0

i = 0
while i < n:
    if nums[i] == 1:
        answer += 1
        i += 1
    elif i + 1 < n and nums[i+1] == 1:
        answer += nums[i]
        i += 1
    elif i == n -1:
        answer += nums[i]
        break
    elif nums[i] > 1 and nums[i+1] > 1:
        answer += nums[i] * nums[i+1]
        i += 2
    elif nums[i] <= 0:
        minus = nums[i:]
        break

while True:
    lenMinus = len(minus)
    if lenMinus >= 2:
        answer += minus[0] * minus[1]
        minus.pop(0)
        minus.pop(0)
    elif lenMinus == 1:
        answer += minus[0]
        break
    else:
        break

print(answer)