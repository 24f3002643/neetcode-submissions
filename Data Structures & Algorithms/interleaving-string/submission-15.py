# Bottom Up DP (Tablulation)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        m = len(s1)
        n = len(s2)
        cache = [[None for i in range(n+1)] for j in range(m+1)]
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i == m and j == n:
                    cache[i][j] = True
                    continue
                cache[i][j] = (i < m and s1[i] == s3[i+j] and cache[i+1][j]) or (j < n and s2[j] == s3[i+j] and cache[i][j+1])
        return cache[0][0]