# Memoization
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        m = sum(nums)
        n = len(nums)
        cache = [[None for i in range(2*m+1)] for i in range(n)]
        return self.recurse(nums,target, 0, 0, cache)
    
    def recurse(self, nums, target, i, curr_sum, cache):
        if cache[i][curr_sum] is not None:
            return cache[i][curr_sum]
        if i == len(nums)-1:
            if curr_sum + nums[i] == target:
                cache[i][curr_sum] = 1
                return 1
            else:
                cache[i][curr_sum] = 0
                return 0
        
        result1 = self.recurse(nums, target, i+1, curr_sum+nums[i], cache)
        result2 = self.recurse(nums, target, i+1, curr_sum-nums[i],
        cache)
        cache[i][curr_sum] = result1 + result2
        return result1 + result2
        

        