## Brute Force
- Will need to check every array with every other array.


ALGORITHM :
- new_array = []
- n = len(array)
- isMerged = [False for i in range(n)]
- for i in range(len(array)):
-    if isMerged[i]:
-       continue
-   updated = [array[i][0], array[i][1]]
-   for j in range(i+1, len(array)):
-       if overlap(array[i], array[j])
-           updated[0] = min(array[j][0], updated[0])
-           updated[1] = max(array[j][1], updated[1])
-           isMerged[j] = True
-   new_array.append(updated)
-   isMerged[i] = True
- return new_array

The above approach fails in a case, where for a given ith array, a jth array does not directly overlap, but overlap with new array when directly overlapped arrays are merged.
    - As per my analysis, detecting undirectly overlapped arrays is not possible in one single pass. This is because indirectly overlapped will show overlap, when all the directly overlapping array have been merged, which requires a single pass.
    


ALGORITHM :
```python
def merge(intervals):
    final_array = []
    n = len(intervals)
    isMerged = [False for i in range(n)]
    flag = False
    while
```
Complexity
- Space Complexity : O(n), where n is the size of the array.
- Time Complexity : O(n2)
