Minimum_Path_Effort(heights):
- find min height
- find max height
- low = 0
- high = max height - min height
- while low <= high :
-   mid = (low + high) / 2 
-   if canReach(heights, mid)
-       high = mid - 1
-   else
-       low = mid + 1
- return low

canReach(heights, E):
- set a visited array with all value initialized to False
- return dfs(heights,E, 0,0, visited)

dfs(heights, E,row, col, visited)
- visited[row][col] = True
- if row == len(heights) -1 and col == len(heights[0])- 1:
-       return True
- for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
-   next_row = row + dr
-   next_col = col + dc
-   if 0<= next_row < len(heights) and 0 <= next_col < len(heights[0]) and not visited[next_row][next_col]:
-       if abs(heights[row][col] - heights[next_row][next_col]) > E:
-           continue
-       result =  dfs(heights, E, next_row, next_col, visited)
-       if result :
-           return True
- return False   
   
1. Initially, I missed putting dfs return value in result and checking for result. 
2. If the recursive call return True, that means destination has been found. The current dfs need to propagate that result upward.

bfs(heights, E, visited):
 - q = Queue()
 - q.enque((0,0))
 - visited[0][0] = True
 - While q is not empty:
    - cell = q.deque()
    - if cell[0] == len(heights) - 1 and cell[1] == len(heights[0]) - 1:
    -       return True
    - for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
    -   next_row = cell[0] + dr
    -   next_col = cell[1] + dc
    -   if 0<= next_row < len(heights) and 0 <= next_col < len(heights[0]) and not visited[next_row][next_col]:
    -       if abs(heights[cell[0]][cell[1]] - heights[next_row][next_col]) > E:
    -           continue
    -       q.enque((next_row, next_col))
    -       visited[next_row][next_col] = True
    - 
- return False   
   
1. One important thing to note here in bfs implementation is that the cell should be marked as visited while enqueing and not dequeing.
2. This is because a cell can get added to queue multiple time before its first dequing since not visited condition will hold True.

- There are two variants of binary search here :
    1. low < = high
    2. low < high 
- Case 1 :
    1. When the loop terminates, the pointers have crossed `high < low`.
    2. At that point, height is the largest infeasible value, and low is the smallest feasible value.
- Case 2 :
    1. The updates will change
```python
    if canReach(mid):
        high = mid
    else:
        low = mid + 1
```
    3. The answer is always somewhere in `[low, high]`
    4. If mid is feasible, mid itself could be the answer, so you must keep it: `high = mid`
    5. If mid is infeasible, mid cannot be the answer, so discard it: `low = mid + 1`
    6. Eventually: `low == high` and that single remaining value is the smallest feasible `E`.

code :
```python
from collections import deque 

def minimumEffortPath(heights):
    rows, cols = len(heights), len(heights[0])
    min_height = min[min(heights[i]) for i in range(rows)]
    max_height = max[max(heights[i]) for i in range(rows)]
    low = 0
    high = max_height - min_height
    while low <= high :
        mid = (low + high) // 2
        if canReach(heights, mid):
            high = mid - 1
        else :
            low = mid + 1
    return low

def canReach(heights, E):
    visited = [[False]* cols for i in range(rows)]
    return depth_first_search(heights, E, 0, 0, visited)

def depth_first_search(heights, E, row, col, visited):
    visited[row][col] = True
    if row == len(heights) - 1 and col == len(heights[0]) - 1:
        return True
    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            next_row = row + dr
            next_col = col + dc
            if 0 <= next_row < len(heights) and 0 <= next_col < len(heights[0]) and not visited[next_row][next_col]:
                if abs(heights[row][col] - heights[next_row][next_col]) > E :
                    continue
                result = depth_first_search(heights, E, next_row, next_col, visited)
                if result:
                    return True
    return False

def breadth_first_search(heights, E, visited):
    queue = deque()
    queue.append((0,0))
    visited[0][0] = True
    while queue:
        row, col = queue.popleft()
        if row == len(heights) - 1 and col == len(heights[0]) - 1:
            return True
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            next_row = row + dr
            next_col = col + dc
            if 0 <= next_row < len(heights) and 0 <= next_col < len(heights[0]) and not visited[next_row][next_col]:
                if abs(heights[row][col] - heights[next_row][next_col]) > E :
                    continue
                queue.append((next_row, next_col))
                visited[next_row][next_col] = True
    return False

```
