## Approach
1. We need a way divide the entire array into 4 parts, like finding the index length-wise and breadth-wise that divides them into halves.
2. Within each subparts, check  if all values are same :
    - If yes, set `isLeaf` to True and set `val` to value of grid, and then stop.
    - If no, set `isLeaf` to False, and set `val` to any value, and then recursively divide this current sub-parts into 4 smaller subparts.
3. return node


## Algorithm
Construct(grid):
- r1, r2 = 0, len(grid)-1
- c1, c2 = 0, len(grid[0])-1
- root = constructQuadTree(grid, r1, r2, c1, c2)
- return root 

constructQuadTree(grid, r1, r2, c1, c2):
- root = Node()
- rep_cell = grid[r1][c1]
- mid_row = (r1+r2)//2
- mid_col = (c1+c2)//2
- for i in range(r1, r2+1):
-   for j in range(c1, c2+1):
-       if grid[i][j] == rep_cell:
-           continue
-       else:
-           root.isLeaf = False
-           root.val = 0
-           root.topLeft = constructQuadTree(grid, r1, mid_row, c1, mid_col)
-           root.topRight = constructQuadTree(grid, r1, mid_row, mid_col+1, c2)
-           root.bottomLeft = constructQuadTree(grid, mid_row+1, r2, c1, mid_col)
-           root.bottomRight = constructQuadTree(grid, mid_row+1, r2, mid_col+1, c2)
-           return root
- root.isLeaf = True
- root.val = rep_cell
- root.topLeft = null
- root.topRight = null
- root.bottomLeft = null
- root.bottomRight = null
- return root


## Python Code
```python
def construct(grid):
    r1, r2 = 0, len(grid)-1
    c1, c2 = 0, len(grid[0])-1
    root = constructQuadTree(grid, r1, r2, c1, c2)
    return root 
    
def constructQuadTree(grid, r1, r2, c1, c2):
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

                root.topLeft = constructQuadTree(
                    grid, r1, mid_row, c1, mid_col
                )
                root.topRight = constructQuadTree(
                    grid, r1, mid_row, mid_col + 1, c2
                )
                root.bottomLeft = constructQuadTree(
                    grid, mid_row + 1, r2, c1, mid_col
                )
                root.bottomRight = constructQuadTree(
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
```

## Complexity
### Time Complexity
```
# The below time complexity is clear, but  the language is not clear.
- In the worst case, every cell of the grid need to be visited to check the value its contains. So this becomes `O(n2)`.
- Also, each cell will be checked at most `log n` times, in the worst case.
- This makes it `O(n2 log n)`
```

- At each recursion level, the total number of cells that will be checked across all regions is at most `O(n2)`.
- The grid can be divided in half along each dimension at every level, giving `O(log n)` levels.
- Therefore, the worst case time complexity is `O(n2 log n)`

### Space Complexity
- `O(log n)` due to recursion stack.
- `O(n2)` due to quad tree that will be formed.
- This makes space complexity `O(n2)` in worst case.
