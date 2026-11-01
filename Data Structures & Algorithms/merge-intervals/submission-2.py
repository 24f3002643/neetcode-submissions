class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        new_array = []
        n = len(intervals)
        isMerged = [False for i in range(n)]
        for i in range(n):
            if isMerged[i]:
                continue
            merged = [intervals[i][0], intervals[i][1]]
            for j in range(i+1,n):
                if self.isOverlap(intervals[i], intervals[j]):
                    merged[0] = min(merged[0], intervals[j][0])
                    merged[1] = max(merged[1], intervals[j][1])
                    isMerged[j] = True
            new_array.append(merged.copy())
            isMerged[i] = True
            merged.clear()
        return new_array


    def isOverlap(self, arr1, arr2):
        a = arr1[0]
        b = arr1[1]
        c = arr2[0]
        d = arr2[1]
        return (a <= c and c <= b) or (a <= d and d <= b)

        