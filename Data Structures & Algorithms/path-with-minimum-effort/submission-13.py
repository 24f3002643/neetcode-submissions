import sys

# Set Python's internal recursion cap to a high value
sys.setrecursionlimit(10**6) 

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        visited = [[False] * cols for _ in range(rows)]
        min_effort = float('infinity')
        min_effort = self.explore(heights, min_effort, visited, 0,0, 0) #        starting from (0,0)
        return min_effort

    def explore(self, heights, min_effort, visited, row, col, current_effort):
        visited[row][col] = True
        if row == len(heights) - 1 and col == len(heights[0]) - 1: # if current cell is the destination
            visited[row][col] = False
            min_effort = min(min_effort, current_effort)
            return min_effort
        if current_effort >= min_effort:
            visited[row][col] = False
            return min_effort
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            next_row = row + dr
            next_col = col + dc
            if 0 <= next_row < len(heights) and 0 <= next_col < len(heights[0]) and not visited[next_row][next_col] : # checking if the neighbour is within the boundary of matrix
                edge_diff = abs(heights[row][col] - heights[next_row][next_col])
                new_effort = max(current_effort, edge_diff)
                min_effort = self.explore(heights, min_effort, visited, next_row, next_col, new_effort)
        visited[row][col] = False
        return min_effort
        
