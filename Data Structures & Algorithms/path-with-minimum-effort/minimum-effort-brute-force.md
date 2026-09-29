class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        visited = [[False] * cols for _ in range(rows)]
        
        def search(
        

Minimum_Path_Effort(heights):
1. find rows and cols of the matrix
2. set a visited array with all values as False
3. set two variables r = 0 and c = 0
4. mark the cell (0,0) as visited
5. set a variable min_effort = infinity
6. run a while loop till r < rows and c < cols# till we reach the end of graph or boundary of graph
6.1     current_effort = infinity   
8.1     if not visited[nr, nc]:   
9.          current_effort = explore(heights, r, c, current_effort) # start exploration from the adjacent cell
10.         if current_effort < min_effort: # update the minimum effort
11.              min_effort = current_effort
12.              continue
13.          else:
14.              visited[nr,nc] = False # if no improvement in current effort, then backtrack


explore(heights, r, c, current_effort):
1. visited[nr][nc] = True
1.1 if r==rows-1 and c = cols-1 :   
1.2     return current_effort   
2.      for (dr,dc) in [(1,0),(-1,0),(0,1),(0,-1)]
3.          nr = r + dr, nc = c + dc
4.              if not visited[nr, nc]:
5.                  if abs(heights[r,c] - heights[nr,nc]) < current_effort:   
5.1                     current_effort = heights[nr][nc] - heights[r][c]
6.                      explore(heights, nr, nc, current_effort)
7.                  else:
8.                      explore(heigts, r, c, current_effort)


explore(r,c,current_effort):
1. visited[r][c] = True 
2. if r == rows-1 and c == cols -1 :
3.      min_effort = min(min_effort, current_effort)
4.      return # reached the end of matrix, so need to return
5. for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
6.      nr = r + dr, nc = c + dc
7.      if nr < rows and nc < cols and not visited[nr][nc]:
8.          edge_diff = abs(heights[r][c] - heights[nr][nc])
9.          current_effort = max(edge_diff, current_effort)
10.             explore(nr, nc, current_effort)
11.         visited[r][c] = False




explore(r,c, current_effort):
1. set visited[r][c] = True
2. if heights[r][c] is the last cell of matrix:
3.      set the min_effort of the minimum between min_effort and current_effort
4.      return
5. for one adjacent cell out of 4 adjacent cell:
6.      if adjacent cell is within the matrix, and is not visited
7.          find edge_diff between current cell and adjacent cell
8.          update the current_effort to maximum of current_effort and edge_diff
9.          explore(adjacent cell.row, adjacent cell.col, current_effort)
10.         mark the current cell[r][c] as unvisited


minimum_path_effort(heights):
1. Get rows, cols
2. create visited 2-d array with all element set to False
3. set min_effort = infinity
4. explore(0,0,0)
5. return min_effort


explore(r,c, current_effort):
1. mark current cell visited
2. if destination:
2.1     mark current cell unvisited
3.      update min_effort
4.      return   
4.1 if  current_effort >= min_effort:   
4.2     mark current cell unvisited   
4.3     return   
5. for each neighbour:
6.      if valid and unvisited:
7.          edge_diff = difference of heights of current cell and the neighbour         
8.          new_effort = max(current_effort, edge_diff)
9.          explore(neighbor.row, neigbour.col, new_effort)
10. mark current cell unvisited


Core Idea of Brute Force :
- The real brute force is typically going to explode exponentially, because the number of path will be very very large, because the problem allow to move in all direction. Has the movement been restricted to only right or only down, then somewhat number of path could have been controlled. Important thing to notice here is in first case, the total number of path is not n*n.
- So we start with brute force but with the trick that we will explore overlapping path at once via backtracking, instead of exploring all possible path independently.
- So here is what we do:
  1. We start from (0,0) via explore().
  2. We mark the current cell as visited.
  3. Then we check if we reached the destination. If yes, then we need to backtrack, in order to check if there exist another path with even less minimum effort. For that, we mark the destination unvisited and backtrack.
  4. Then we check if the current effort is greater or equal to min_effort already found. If yes, then there is no need to continue along that path, since the current effort is only going to increase, not decrease (since current effort is max of differences between cells on that path). So we backtrack. Actually here it is branch and bound, since we pruned the path, since the current effort on path was greater than already found minimum effort. One important thing to note here is, that we checked even for equality, not just greater than here. It make sense here because we are just interested only in calculating the minimum effort overall, and not the paths on which this minimum effort exist. And since the current effort is only going to increase, and currently is equal to min_effort already found, so we can ignore this path.
  5. Then we go the unvisited neighbour cell, and calculate the edge difference, and calculate new effort which is equal to maximum of current_effort and edge_diff. 
  6. Then we again explore() from that neighbour cell.
  7. Also, when the control return from the explore() to the current neighbour cell, we mark the current cell as unvisited in order to make sure that this cell comes in the path in later exploration from another cell.
  
A small improvement to 2nd point :
There are paths which share prefixes, and then have there own branch. So what backtracking (via dfs) does is that it explore one path independently, and then come back at the decision point (point where the branch got separated), and restore the state at this point and then they explore the another branch independently.

python code :
```python
def minimum_path_effort(heights):
    rows, cols = len(heights), len(heights[0])
    visited = [[False] * cols for _ in range(rows)]
    min_effort = float('infinity')
    min_effort = explore(heights, min_effort, visited, 0,0, 0) #        starting from (0,0)
    return min_effort

def explore(heights, min_effort, visited, row, col, current_effort):
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
            min_effort = explore(heights, min_effort, visited, next_row, next_col, new_effort)
    visited[row][col] = False
    return min_effort # I missed this line earlier. This is important, when the function return from non-pruned, non-destination call. Else the function will return None causing comparison will None and int, thus causing error and termination.
        
```
        
    
    
