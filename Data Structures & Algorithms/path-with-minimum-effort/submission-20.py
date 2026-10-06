import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        pq = [] # priority queue
        rows, cols = len(heights), len(heights[0])
        visited = [[False] * cols for i in range(rows)]
        effort = [[float('infinity')] * cols for i in range(rows)] # float('inf') can also work
        effort[0][0] = 0
        # setting up values of priority queue
        # the heap represents the vertices/candidates that are currently available to be processed. Initially, only source is available
        heapq.heappush(pq, (0,0,0))
        # no need to create an edge matrix. For a vertex, we will directly check for edge by going in direction [(1,0), (-1,0), (0,1), (0,-1)] 
        while True:
            vertex = heapq.heappop(pq)
            row, col = vertex[1], vertex[2]
            if visited[row][col]:
                continue
            visited[row][col] = True
            if row == rows - 1 and col == cols - 1:
                return effort[row][col]
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                next_row = row + dr
                next_col = col + dc
                if  0 <= next_row < rows and 0 <= next_col <cols and not visited[next_row][next_col]:
                    new_effort = max(effort[row][col], abs(heights[row][col] - heights[next_row][next_col]))
                    if new_effort < effort[next_row][next_col]:
                        effort[next_row][next_col] = new_effort
                        heapq.heappush(pq, (new_effort, next_row, next_col))