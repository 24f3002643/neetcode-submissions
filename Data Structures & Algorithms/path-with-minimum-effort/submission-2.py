import sys

# Set Python's internal recursion cap to a high value
sys.setrecursionlimit(10**6) 
# Brute Force Approach
# Traverse through all the path (there will be total of n*n paths)
# Keep track of min_diff 
# return the min_diff

# Two correction needed in this brute force
# 1. There are not only n*n paths. A path can wander, backtrack into unvisited cells, take detours, etc. The actual number of simple paths grows exponentially with the number of cells. I need to have  a visited-unvisitd set to avoid infinite loops.
# 2. I need to track max of path, not difference of path. I need to take max along one path, and then minimize that max across all paths.

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        self.result = float('inf')
        visited = [[False] * cols for _ in range(rows)]

        def dfs(r, c, max_so_far):
            if r == rows - 1 and c == cols - 1:
                self.result = min(self.result, max_so_far)
                return
            visited[r][c] = True
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    diff = abs(heights[dr][dc] - heights[r][c])
                    new_max = max(max_so_far, diff)
                    if new_max < self.result :
                        dfs(nr, nc, new_max)
            visited[r][c] = False
        dfs(0,0,0)
        return self.result

        