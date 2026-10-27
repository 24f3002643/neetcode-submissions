import sys
sys.setrecursionlimit(10000)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        return self.recurse(s1,s2,s3,0,0,0)
    
    def recurse(self, s1, s2, s3, i, j, k):
        path1 = 0
        path2 = 0
        if i+j == len(s3):
            return True
            # if i == len(s1) and j == len(s2):
            #     return True
            # else:
            #     return False
        if i < len(s1) and s3[k] == s1[i]:
            path1 = self.recurse(s1,s2,s3,i+1,j,i+j+1)
        if j < len(s2) and s3[k] == s2[j]:
            path2 = self.recurse(s1,s2,s3,i,j+1,i+j+1)
        if path1 or path2:
            return True
        else:
            return False