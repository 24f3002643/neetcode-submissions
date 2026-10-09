# Brute Force with Memoization
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = [None] * len(s)
        return self.dfs(s, wordDict, 0, cache)
    
    def dfs(self, s, wordDict, start, cache):
        if start == len(s):
            return True
        if cache[start] is not None:
            return cache[start]
        else :
            for end in range(start + 1, len(s)+1): # we need len(s)+1 to include 1 more than the last valid index to keep slicing correct
                if s[start:end] in wordDict:
                    if self.dfs(s, wordDict, end, cache) == True:
                        cache[start] = True
                        return True
            cache[start] = False
            return False