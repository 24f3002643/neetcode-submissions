from collections import deque
import sys

# Set Python's internal recursion cap to a high value
sys.setrecursionlimit(10**6) 
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        min_height = min(min(heights[i]) for i in range(rows))
        max_height = max(max(heights[i]) for i in range(rows))
        low = 0
        high = max_height - min_height
        while low <= high :
            mid = (low + high) // 2
            if self.canReach(heights, mid):
                high = mid - 1
            else :
                low = mid + 1
        return low


    def canReach(self, heights, E):
        rows, cols = len(heights), len(heights[0])
        visited = [[False]* cols for i in range(rows)]
        return self.breadth_first_search(heights, E, visited)

    def depth_first_search(self, heights, E, row, col, visited):
        visited[row][col] = True
        if row == len(heights) - 1 and col == len(heights[0]) - 1:
            return True
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                next_row = row + dr
                next_col = col + dc
                if 0 <= next_row < len(heights) and 0 <= next_col < len(heights[0]) and not visited[next_row][next_col]:
                    if abs(heights[row][col] - heights[next_row][next_col]) > E :
                        continue
                    result = self.depth_first_search(heights, E, next_row, next_col, visited)
                    if result:
                        return True
        return False


    def breadth_first_search(self, heights, E, visited):
        queue = deque()
        queue.append((0,0))
        visited[0][0] = True
        if queue:
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
    