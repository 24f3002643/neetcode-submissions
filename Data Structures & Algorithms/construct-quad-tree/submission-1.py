"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        r1, r2 = 0, len(grid)-1
        c1, c2 = 0, len(grid[0])-1
        root = self.constructQuadTree(grid, r1, r2, c1, c2)
        return root 
    
    def constructQuadTree(self,grid: List[List[int]], r1, r2, c1, c2):
        root = Node(False, False, None, None, None, None)
        rep_cell = grid[r1][c1]

        mid_row = (r1 + r2) // 2
        mid_col = (c1 + c2) // 2

        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if grid[i][j] == rep_cell:
                    continue
                else:
                    root.isLeaf = False
                    root.val = False

                    root.topLeft = self.constructQuadTree(
                        grid, r1, mid_row, c1, mid_col
                    )
                    root.topRight = self.constructQuadTree(
                        grid, r1, mid_row, mid_col + 1, c2
                    )
                    root.bottomLeft = self.constructQuadTree(
                        grid, mid_row + 1, r2, c1, mid_col
                    )
                    root.bottomRight = self.constructQuadTree(
                        grid, mid_row + 1, r2, mid_col + 1, c2
                    )

                    return root

        root.isLeaf = True
        root.val = rep_cell
        root.topLeft = None
        root.topRight = None
        root.bottomLeft = None
        root.bottomRight = None

        return root