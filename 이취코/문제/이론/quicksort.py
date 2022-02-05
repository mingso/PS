# 쉬운 버전
def quick_sort(array, start, end):
    if start >= end :
        return
    pivot = start
    left = start + 1
    right= end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right :
            array[right], array[pivot] = array[pivot], array[right]
        else :
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

# pythonic한 버전
def quick_sort_pythonic(array):
    if len(array) <= 1:
        return array

    pivot = array[0]    # 첫번째 원소를 pivot으로
    tail = array[1:]    # 피벗 제외 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    return quick_sort_pythonic(left_side) + [pivot] + quick_sort_pythonic(right_side)

array = [ 5, 7, 9, 0, 3, 1, 5, 2, 4, 8]

quick_sort(array, 0, len(array) - 1)
print(array)