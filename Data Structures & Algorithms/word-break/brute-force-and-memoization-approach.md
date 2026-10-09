## AlGORITHM 
WORD-BREAK(s, wordDict, start)
- if start == s.length
- return True
- for end from start + 1 to s.length
-   flag = false
-   if s[start:end] exists in wordDict
-       flag = WORD-BREAK(s, wordDict, end) // flag can be removed and directly the result value can be compared
-       if flag == true 
-           return True
- if flag is False
-   return False

##  Imporved Brute Force Algorithm
WORD-BREAK(s, wordDict, start, memo)
- if start == s.length
-   return True
- if start exist in memo
-   return memo[start]
- else
-   for end from start + 1 to s.length
-       if s[start:end] exists in wordDict
-           if WORD-BREAK(s, wordDict, end, memo) == True
-               memo[start] = True
-               return True
-   memo[start] = False
-   return False

memo[start] = true : Means that at least one valid segmentation was found.
memo[start] = false : Means that every possible prefix from start was tried, and none led to a complete segmentation.
so memo[start] stores the final value for substring starting from index start

```python
def wordBreak(s, wordDict):
    cache = [None] * len(s)
    return dfs(s, wordDict, 0, cache)

def dfs(s, wordDict, start, cache):
    if start == len(s):
        return True
    if cache[start] is not None:
        return cache[start]
    else :
        for end in range(start + 1, len(s)+1): # we need len(s)+1 to include 1 more than the last valid index to keep slicing correct
            if s[start:end] in wordDict:
                if dfs(s, wordDict, end, cache) == True:
                    cache[start] = True
                    return True
        cache[start] = False
        return False
```
