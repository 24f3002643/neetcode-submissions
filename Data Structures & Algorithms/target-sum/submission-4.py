# Memoization
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        m = sum(nums)
        n = len(nums)
        cache = {i: dict(zip(range(-m,m+1), [None for j in range(2*m+1)])) for i in range(-1,n)}
        return self.recurse(nums,target, -1, 0, cache)
    
    def recurse(self, nums, target, i, curr_sum, cache):
        if cache[i][curr_sum] is not None:
            return cache[i][curr_sum]
        if i == len(nums)-1:
            if curr_sum == target:
                cache[i][curr_sum] = 1
                return 1
            else:
                cache[i][curr_sum] = 0
                return 0
        
        result1 = self.recurse(nums, target, i+1, curr_sum+nums[i+1], cache)
        result2 = self.recurse(nums, target, i+1, curr_sum-nums[i+1],
        cache)
        cache[i][curr_sum] = result1 + result2
        return result1 + result2
        

        