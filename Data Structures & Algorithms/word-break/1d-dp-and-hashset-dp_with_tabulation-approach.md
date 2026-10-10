## Bottom up DP (Tabulation) approach
- dp[i] = whether s[i:] can be segemented or not.
- The base case is dp[n] = True, where n = len(s)
- We will fill the dp, from right to left because dp[i] depends on dp[j], where j > i.
- At every index i, we try every possible endpoints j from i+1 to n. If both below conditions holds, then dp[i] = True :
    1. s[i:j] is in wordDict.
    2. dp[j] == True
    
Algorithm :
WORD-BREAK(s, wordDict):
- n = s.length
- dp = [None] * n
- dp[n] = True
- for i from n-1 down to 0
-   for j from i to n
-       if s[i:j] is in wordDict and dp[j] == True
-           dp[i] =True
- return dp[0]

There are three errors :
1. the length of dp array should be n+1, and not n.
2. Initialize dp with False, so that indices with no valid segmentation remain False.
3. Start j at i+1 to consider non-empty substrings. However, starting j from i is completely fine.
4. Insert a break statement inside the loop, to avoids rechecking more substrings once dp[i] is known to be True.

Corrected algorithm:
WORD-BREAK(s, wordDict):
- n = s.length
- dp = [False] * (n+1)
- dp[n] = True
- for i from n-1 down to 0
-   for j from i+1 to n
-       if s[i:j] is in wordDict and dp[j] == True
-           dp[i] =True
-           break
- return dp[0]

Code
```python
def wordBreak(s, wordDict):
    n = len(s)
    wordDict = set(wodDict) #the list has been converted into set for faster lookup
    dp = [False] * (n+1)
    dp[n] = True
    for i in (n-1, -1, -1):
        for j in (i+1, n+1):
            if s[i:j] in wordDict and dp[j] == True:
                dp[i] = True
                break
    return dp[0]
```

