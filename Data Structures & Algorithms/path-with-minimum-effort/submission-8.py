class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        # union find helpers
        parent = list(range(rows * cols))
        rank = [0] * (rows * cols)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1
            return True
        
        # collect all edges (u,v,weights)
        edges = []
        for r in range(rows):
            for c in range(cols):
                idx = r * cols + c
                if c + 1 < cols:
                    nidx = r * cols + (c + 1)
                    w = abs(heights[r][c] - heights[r][c+1])
                    edges.append((w, idx, nidx))
                if r + 1 < rows:
                    nidx = (r + 1) * cols + c
                    w = abs(heights[r][c] - heights[r+1][c])
                    edges.append((w, idx, nidx))
        
        edges.sort()

        start, end = 0, rows * cols - 1
