import sys

def dist(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def mergeSort(start, end):
    global minDist
    if start < end:
        mid = (start + end) // 2
        minDist = min(mergeSort(start, mid), mergeSort(mid+1, end))

    elif start == end:
        return dist(points[start], points[end])




n = int(sys.stdin.readline())
points = []
for _ in range(n):
    points.append(tuple(map(int, sys.stdin.readline().split())))

points.sort()
print(points)

minDist = sys.maxsize

mergeSort(0, n-1)