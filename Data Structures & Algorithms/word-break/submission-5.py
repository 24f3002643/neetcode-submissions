# Bottom Up DP with hashing
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordDict = set(wordDict) #the list has been converted into set for faster lookup
        dp = [False] * (n+1)
        dp[n] = True
        for i in range(n-1, -1, -1):
            for j in range(i+1, n+1):
                if s[i:j] in wordDict and dp[j] == True:
                    dp[i] = True
                    break
        return dp[0]