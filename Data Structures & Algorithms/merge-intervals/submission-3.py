class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals = sorted(intervals, key = lambda x : x[0])
        new_array = []
        for i in range(n):
            if i == 0:
                new_array.append(intervals[i].copy())
                continue
            last_appended_array = new_array[-1]
            if last_appended_array[1] >= intervals[i][0]:
                last_appended_array[1] = max(last_appended_array[1], intervals[i][1])
            else:
                new_array.append(intervals[i].copy())
        return new_array
            
        