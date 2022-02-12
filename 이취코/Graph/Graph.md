## DFS
### 1. DFS 알고리즘
최대한 깊이 내려간 뒤, 더 이상 깊이 갈 곳이 없을 경우 옆으로 이동

즉, 루트 노드에서 시작해서 다음 branch로 넘어가기 전에 해당 branch를 완벽하게 탐색하는 방식.

### 2. 특징
- 모든 노드를 방문하고자 하는 경우
- BFS에 비해 간단하지만 속도는 느림
- 스택 또는 재귀함수로 구현

### 3. 기본 코드
```python
def DFS_with_adj_list(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            # stack += set(graph[n]) - set(visited)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort(reverse=True)
                stack += temp
    return visited
  
graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1

print(DFS_with_adj_list(graph_list, root_node))
```

---

## BFS
### 1. BFS 알고리즘
최대한 넓게 이동한 다 음, 더 이상 갈 수 없을 때 아래로 이동.

즉, 루트 노드에서 시작해서 인접한 노드를 먼저 탐색하는 방법으로, 시작 정점으로부터 가까운 정점을 먼저 방문하고 멀리 떨어져 있는 정점을 나중에 방문하는 순회 방법입니다.

### 2. 특징
- 주로 두 노드 사이의 최단 경로를 찾을 때 사용
- Queue를 사용해서 구현
- 인접 행렬보다 인접 리스트를 사용하는 방식이 시간적으로 효율적.

### 3. 기본 코드
```python
from collections import deque

def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft() #pop(0)은 시간 복잡도가 O(N)이라 deque를 사용
        if n not in visited:
            visited.append(n)
            # queue += set(graph[n]) - set(visited)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort()
                queue += temp
    return visited
  
graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1

print(BFS_with_adj_list(graph_list, root_node))
```

---

## Cycle
DFS를 수행하면서 방문한 정점을 기록합니다. 방문한 정점을 또 방문하면 cycle이 존재합니다.




[출처]
- https://devuna.tistory.com/32
- https://cyc1am3n.github.io/2019/04/26/bfs_dfs_with_python.html
