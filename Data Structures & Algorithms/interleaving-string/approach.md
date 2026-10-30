## Brute Force Approach
- The key idea is to check all the possible interleaving combination of string s1 and s2. Recursion will be needed for both.
- So, at each recursive step, explore each valid choice from s1 and s2( There may be zero, one, or two valid choices).
    - if the character at current index in s3 matches current index being processed in s1, then choose the character of s1.
    - if the character at current index in s3 matches current index being processed in s2, then choose the character of s2.
- if either of these branch return true, then return true, else return false.
- the base case would be that current index being processed in s1 and s2 have become equal to their length respectively. If yes, then return true.

## Brute Force Without Memoization
```python
def isInterleave(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False
    return recurse(s1,s2,s3,0,0)
    
def recurse(s1,s2,s3,i,j):
    # i and j are the index that are to be checked currently.
    # So base case is when they have reached their end i.e. have become equal to their respective length.
    if i == len(s1) and j == len(s2) : 
        return True
    k = i + j
    if i < len(s1) and s3[k] == s1[i]:
        if recurse(s1,s2,s3,i+1,j):
            return True
    if j < len(s2) and s3[k] == s2[j]:
        if recurse(s1,s2,s3,i,j+1):
            return True
    return False
```

### Complexity
- let m = len(s1) and n = len(s2)
- Time : O(2^(m+n))
- Space : O(m+n) for the recursion stack


## Brute Force With Memoization
```python
def isInterleave(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False
    # memo = [[None] * len(s2)+1] * (len(s1)+1)
    # This makes every row reference the same list. 
    #Use a list comprehension to create independent rows.
    memo = [[None for i in range(len(s2)+1)] for j in range(len(s1)+1)]
    return recurse(s1,s2,s3,0,0, memo)
    
def recurse(s1,s2,s3,i,j, memo):
    if memo[i][j] is not None:
        return memo[i][j]
    
    if i == len(s1) and j == len(s2) : 
        memo[i][j] = True
        return True
    k = i + j
    if i < len(s1) and s3[k] == s1[i]:
        if recurse(s1,s2,s3,i+1,j, memo):
            memo[i][j] = True
            return True
    if j < len(s2) and s3[k] == s2[j]:
        if recurse(s1,s2,s3,i,j+1, memo):
            memo[i][j] = True
            return True
    memo[i][j] = False
    return False
```

### Complexity
- let m = len(s1) and n = len(s2)
- Time : O(mn)
- Space : O(mn) for the memoization table, plus (O(m+n) for the recursion stack. Total: O(mn+m+n).

## Bottom-Up DP (Tabulation)
- This will require traversing from end to start of string s1 and s2.

Calculation :
- cache[i][j] = 
    - TRUE, if i==len(s1) and j == len(s2)
    - (TRUE and cache[i+1][j], if i < len(s1) and s1[i]==s3[i+j]) or (TRUE and cache[i][j+1], if j < len(s2) and s2[j]==s3[i+j])
    - FALSE, Otherwise
    
```python
def isInterleave(s1,s2,s3):
    if len(s1) + len(s2) != len(s3):
        return False
    m = len(s1)
    n = len(s2)
    cache = [[None for i in range(n+1)] for j in range(m+1)]
    cache[m][n] = True
    for i in range(m, -1, -1):
        for j in range(n, -1, -1):
            if i == m and j == n:
                cache[i][j] = True
                continue
            cache[i][j] = (i < m and s1[i] == s3[i+j] and cache[i+1][j]) or (j < n and s2[j] == s3[i+j] and cache[i][j+1])
    return cache[0][0]
```
### Complexity
- let m = len(s1) and n = len(s2)
- Time : O(mn)
- Space : O(mn)
