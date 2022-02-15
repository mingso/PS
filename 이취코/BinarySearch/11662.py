import sys
def binarySearch(num):
    start, end = 0, n-1
    while start <= end:
        mid = (start + end) // 2
        if hadCards[mid] == num:
            return mid
        elif hadCards[mid] > num:
            end = mid - 1
        elif hadCards[mid] < num:
            start = mid + 1
    return -1

Ax, Ay, Bx, By, Cx, Cy, Dx, Dy = map(int, sys.stdin.readline().split())

disA = ((Bx-Ax) ** 2 + (By-Ay) ** 2) ** 0.5
disB = ((Dx-Cx) ** 2 + (Dy-Cy) ** 2) ** 0.5

print(disA, disB)