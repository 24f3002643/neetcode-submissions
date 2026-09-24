from collections import deque

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        def canReach(mid: int) -> bool:
            visited = [[False] * cols for _ in range(rows)]
            queue = deque([0,0])
            visited[0][0] = True

            while queue:
                r, c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return True
                for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                        diff = abs(heights[nr][nc] - heights[r][c])
                        if diff <= mid:
                            visited[nr][nc] = True
                            queue.append((nr, nc))
            return False
        
        lo, hi = 0, max(max(row) for row in heights)
        while lo < hi:
            mid = (lo + hi) // 2
            if canReach(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

