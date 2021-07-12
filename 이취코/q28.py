n = int(input())

num = list(map(int, input().split()))

def binary_search(i):
    if num[i] > i:
        if i - i//2 != i :
            return binary_search(i - i//2)
        else :
            return -1
    elif num[i] < i:
        if i + i//2 != i:
            return binary_search(i + i//2)
        else:
            return -1
    elif num[i] == i:
        return i

print(binary_search(n//2))
