Idea :
- Idea is to use the dijakstra framework.
- How does dijakstra framework works ? Dijakstra framework says "I  keep the best currently known cost for each vertex. When processing a vertex, I consider its un-finalized neighbours. If the newly discovered path gives a smaller cost for that neighbor I update that neighbor's stored cost.
- Now how dijakstra works :
    1. Suppose a vertex u get popped from priority queue and marked as visited, which means that this vertex u have its cost finalized.
    2. Now, for a single unvisited neighbor v of u, new_distance is calculated as `new_distance = distance[u] + edge_weight(u,v)`. This line calculates the cost of new candidate path that got created by adding v.
    3. Now, we check `if new_distance < distance[v]` i.e. is the newly found distance to neighbour v smaller that the currently known distance to v. If yes, we update `distance[v] = new_distance`. Or in single line what we are doing is `distance[v] = min(distance[v], new_distance)`. 
        - This line checks if the newly found path to reach v is better than already known path to v.
        - That is we are comparing two candidate paths.
    4. Now it may happen in multiple iteration, v gets updated, so what is actually happening that the multiple path that exist to reach v is getting compared and the best one is getting selected.
- So how this fits to this problem :
    1. We will use another variable instead of distance - effort. effort[u] = the minimum possible path effort from the source to v (where the effort of path is the maximum edge weight along that path).
    2. So what we need to find is effort[destination] which will mean the minimum possible path effort from the source to destination, found after comparing against many candidate path.
    3. There needs to be slight change in dijakstra code.
        - new_effort = max(effort[u], edge_weight(u,v)) : This stores the effort of one candiadate path that got created by considering the unvisited neighbour v.
        - effort[v] = min(effort[v], new_effort) : This compare the newly candidate path by another candidate path, and update the effort of v if the newly candidate path provides a better effort to reach v.
    


Minimum_Path_Effort(Height):
1. Create an edge matrix to represent the edge between vertices.
2. create a min priority structure q
3. create a visited array for each vertex
4. mark (0,0) as visited
5. insert (0,0) to q with value 0
6. while q is not empty
7.      vertex = pop element from q
7.1     mark vertex as visited
7.2     if vertex is destination:
7.3         return
8.      for each neighbour of vertex
9.          if neighbour is not visited
10.             if  edge_weight(vertex to neighbour) > q[neighbour]
11.                 set q[neighbour] =  edge_weight(vertex to neighbour)
12. 
