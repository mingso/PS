import sys

def mergeSort(start, end):
    global answer
    if start < end:
        mid = (start + end) // 2
        mergeSort(start, mid)
        mergeSort(mid+1, end)

        a = start
        b = mid + 1
        tmp = []

        while a <= mid and b <= end:
            if nums[a] <= nums[b]:
                tmp.append(nums[a])
                a += 1
            else:
                tmp.append(nums[b])
                b += 1
                answer += mid - a + 1

        if a <= mid:
            tmp = tmp + nums[a:mid+1]
        if b <= end:
            tmp = tmp + nums[b:end+1]

        for i in range(len(tmp)):
            nums[start + i] = tmp[i]

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

answer = 0
mergeSort(0, n-1)

print(answer)
