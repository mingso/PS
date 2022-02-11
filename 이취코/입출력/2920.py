import sys

nums = list(map(int, sys.stdin.readline().split()))

answer = ""
for i in range(len(nums)-1):
    if nums[i] < nums[i+1] and (answer == "" or answer == "ascending"):
        answer = "ascending"
    elif nums[i] > nums[i+1] and (answer == "" or answer == "descending"):
        answer = "descending"
    else:
        answer = "mixed"
        break

print(answer)