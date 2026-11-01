import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = [False for i in range(n)]
        edges = {i:[] for i in range(1,n+1)}
        for (u,v,w) in times:
            edges[u].append((v,w))
        distance, visited = self.dijakstra(edges,k,n, visited)
        for i in visited:
            if i == False:
                return -1
        return max(distance)
    
    def dijakstra(self, edges, source,n, visited):
        distance = [float('inf') for i in range(n)]
        distance[source-1] = 0
        min_heap = []
        heapq.heappush(min_heap, (0,source))
        while min_heap:
            curr_dist, curr_ver = heapq.heappop(min_heap)
            if visited[curr_ver-1]:
                continue
            visited[curr_ver-1] = True
            for v,w in edges[curr_ver]:
                if distance[curr_ver-1] + w < distance[v-1]:
                    distance[v-1] = distance[curr_ver-1] + w
                    heapq.heappush(min_heap,(distance[v-1], v))
        return distance, visited
        

