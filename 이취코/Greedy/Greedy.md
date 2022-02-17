### Greedy 알고리즘 이란?
- 말 그대로 선택의 순간마다 `당장 눈 앞에 보이는 최적의 상황`만을 쫓아 해답에 도달하는 방법

### 탐욕 알고리즘 문제 해결 방법
1. 선택 절차(Selection Procedure) : 현재 상태에서의 최적의 해답을 선택
2. 적절성 검사(Feasibility Check) : 선택된 해가 문제의 조건을 만족하는지 검사
3. 해답 검사(Solution Check) : 원래의 문제가 해결되었는지 검사하고, 해결되지 않았다면 선택 절차로 돌아가 위의 절차를 반복


### 카드 n개 있을 때 조합

#### 1. itertools 이용
```python
from itertools import permutations
from itertools import combinations
items = [1, 2, 3, 4, 5]
list(permutations(items, 2))
# [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '1'), ('2', '3'), ('2', '4'), ('2', '5'),
#  ('3', '1'), ('3', '2'), ('3', '4'), ('3', '5'), ('4', '1'), ('4', '2'), ('4', '3'), ('4', '5'), ('5', '1'), ('5', '2'), ('5', '3'), ('5', '4')]

list(combinations(items, 2))
# [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
```

#### 2. 직접 구현
```python
def permutations(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in permutations(array[:i]+array[i+1:], r-1):
                yield [array[i]] + next
# https://juhee-maeng.tistory.com/91


def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result
    
# 출처: https://programmers.co.kr/learn/courses/4008/lessons/12836
```

---

### 참고
https://hanamon.kr/알고리즘-탐욕알고리즘-greedy-algorithm/