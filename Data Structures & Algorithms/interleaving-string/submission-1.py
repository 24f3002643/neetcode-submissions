class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        return self.recurse(s1,s2,s3,0,0,0)
    
    def recurse(self, s1, s2, s3, i, j, k):
        result = 0
        if k == len(s3):
            return True
        if s3[k] == s1[i]:
            k += 1
            i += 1
            result = self.recurse(s1,s2,s3,i,j,k)
        elif s3[k] == s2[j]:
            k += 1
            j += 1
            result = self.recurse(s1,s2,s3,i,j,k)
        if result:
            return True
        else:
            return False