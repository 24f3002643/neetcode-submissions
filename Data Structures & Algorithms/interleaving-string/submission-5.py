import sys
sys.setrecursionlimit(10000)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1 or not s2 or not s3:
            return True
        if len(s1) + len(s2) != len(s3):
            return False
        return self.recurse(s1,s2,s3,0,0)
    
    def recurse(self, s1, s2, s3, i, j):
        result1 = None
        result2 = None
        if i+j+2 == len(s3):
            return True
        if s3[i+j] == s1[i]:
            result1 = self.recurse(s1,s2,s3,i+1,j)
        if s3[i+j] == s2[j]:
            result2 = self.recurse(s1,s2,s3,i,j+1)
        if result1 or result2:
            return True
        else:
            return False