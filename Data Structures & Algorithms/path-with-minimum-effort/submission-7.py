import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        effort = [[float("inf")] * cols for _ in range(rows)]
        effort[0][0] = 0

        pq = [(0,0,0)]
        visited = [[False] * cols for _ in range(rows)]

        while pq:
            curr_effort, r, c = heapq.heappop(pq)
            
            if visited[r][c]:
                continue
            
            visited[r][c] = True

            if r == rows - 1 and c == cols - 1:
                return curr_effort

            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    diff = abs(heights[nr][nc] - heights[r][c])
                    new_effort = max(curr_effort, diff)
                    if new_effort < effort[nr][nc]:
                        effort[nr][nc] = new_effort
                        heapq.heappush(pq, (new_effort, nr, nc))

        return 0