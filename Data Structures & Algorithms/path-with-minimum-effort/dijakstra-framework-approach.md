Idea :
- Idea is to use the dijakstra framework.
- How does dijakstra framework works ? Dijakstra framework says "I  keep the best currently known cost for each vertex. When processing a vertex, I consider its non-finalized neighbors. If the newly discovered path gives a smaller cost for that neighbor, I update that neighbor's stored cost.
- Now how dijakstra works :
    1. Suppose a vertex u get popped from priority queue and marked as visited (i.e. finalized), which means that this vertex u have its cost finalized.
    2. Now, for a single unvisited neighbor v of u, new_distance is calculated as `new_distance = distance[u] + edge_weight(u,v)`. This line calculates the cost of new candidate path that got created by adding v.
    3. Now, we check `if new_distance < distance[v]` i.e. is the newly found distance to neighbour v smaller that the currently known distance to v. If yes, we update `distance[v] = new_distance`. Or in single line what we are doing is `distance[v] = min(distance[v], new_distance)`. 
        - This line checks if the newly found path to reach v is better than already known path to v.
        - That is we are comparing two candidate paths.
    4. Now it may happen that in multiple iteration v gets updated, so what is actually happening ovrall that the multiple path that exist to reach v is getting compared and the best one is getting selected. [Remember : Dijkstra does not explicitly enumerate all possible paths at once. It discovers candidate paths incrementally.]
- So how this fits to this problem :
    1. We will use another variable instead of distance - effort. effort[u] = the minimum possible path effort from the source to u (where the effort of path is the maximum edge weight along that path).
    2. So what we need to find is effort[destination] which will mean the minimum possible path effort from the source to destination, found after comparing against many candidate path.
    3. There needs to be slight change in dijakstra code.
        - new_effort = max(effort[u], edge_weight(u,v)) : This stores the effort of one candiadate path that got created by considering the unvisited neighbour v. [`effort[u]` already represents the largest edge encountered along the path to u. When we append a new edge, the largest edge in the resulting path is therefore: `max(previous maximum, new edge)`]
        - effort[v] = min(effort[v], new_effort) : This compare the newly considered candidate path by current candidate path, and update the effort of v if the newly candidate path provides a better effort to reach v.
    
[One Thing that I discovered is Origninal Dijakstra is min min optimization problem]

Minimum_Path_Effort(Height):
1. Create an edge matrix to represent the edge between vertices.
3. create a visited array for each vertex
3.1 create a array effort for each vertex initialized to infinity
5. effort[source] = 0
6. while True
7.      vertex = find the unvisited vertex with least value in effort array
7.1     mark vertex as visited
7.2     if vertex is destination:
7.3         return effort[vertex]
8.      for each neighbour of vertex
9.          if neighbour is not visited
10.             new_effort = max(effort[u], edge_weight(u,v))
11.             if new_effort < effort[v]:
12.                 effort[v] = new_effort

```python
import heapq
def minimumPathEffort(heights):
    pq = [] # priority queue
    rows, cols = len(heights), len(heights[0])
    visited = [[False] * cols for i in range(rows)]
    effort = [[0] * cols for i in range(rows)]
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
                new_effort = max(effort[next_row][next_col], abs(heights[row][col] - heights[next_row][next_col]))
                if new_effort < effort[next_row][next_col]:
                    effort[next_row][next_col] = new_effort
                    heapq.heappush(pq, (new_effort, next_row, next_col))
                
                

```
