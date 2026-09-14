'''
Approach :
1. This problem can be thought as a graph problem. Each person represent 
a vertex and trust represents the edges.
2. So we need to find a vertex, with indegree=n-1 and outdegree=0. If such vertex exist, return it, else return -1.
'''
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree={}
        outdegree={}
        #No need of adjacency list here 
        #Alist={} # Adjacenecy list
        for i in range(1,n+1):
            #Alist[i]=[]
            indegree[i]=0
            outdegree[i]=0
        for i,j in trust:
            #Alist[i].append(j)
            indegree[j]+=1
            outdegree[i]+=1
        for i in range(1,n+1):
            if indegree[i]==n-1 and outdegree[i]==0:
                return i
        return -1
