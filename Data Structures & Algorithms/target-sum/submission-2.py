class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.recurse(nums, target, 0, 0)

    def recurse(self, nums, target, i, curr_sum):
        if i==len(nums):
            if curr_sum == target:
                return 1
            else:
                return 0
        result1 = path1 = self.recurse(nums, target, i+1, curr_sum + nums[i])
        result2 = path2 = self.recurse(nums, target, i+1, curr_sum - nums[i])
        return result1 + result2

        