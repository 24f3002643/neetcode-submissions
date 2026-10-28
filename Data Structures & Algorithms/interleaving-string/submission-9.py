# Brute Force With Memoization
import sys
sys.setrecursionlimit(10000)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        # memo = [[None] * len(s2)+1] * (len(s1)+1)
        # This makes every row reference the same list. 
        #Use a list comprehension to create independent rows.
        memo = [[None for i in range(len(s2)+1)] for j in range(len(s1)+1)]
        return self.recurse(s1,s2,s3,0,0, memo)
    
    def recurse(self, s1, s2, s3, i, j, memo):
        if memo[i][j] is not None:
            return memo[i][j]
        
        if i == len(s1) and j == len(s2) : 
            memo[i][j] = True
            return True
        k = i + j
        if i < len(s1) and s3[k] == s1[i]:
            if self.recurse(s1,s2,s3,i+1,j, memo):
                memo[i][j] = True
                return True
        if j < len(s2) and s3[k] == s2[j]:
            if self.recurse(s1,s2,s3,i,j+1, memo):
                memo[i][j] = True
                return True
        memo[i][j] = False
        return False
