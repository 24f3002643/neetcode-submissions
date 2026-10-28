# Brute Force Without Memoization
import sys
sys.setrecursionlimit(10000)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        return self.recurse(s1,s2,s3,0,0)
    
    def recurse(self, s1, s2, s3, i, j):
        if i == len(s1) and j == len(s2) :
            return True
        k = i + j
        if i < len(s1) and s3[k] == s1[i]:
            if self.recurse(s1,s2,s3,i+1,j):
                return True
        if j < len(s2) and s3[k] == s2[j]:
            if self.recurse(s1,s2,s3,i,j+1):
                return True
        return False
