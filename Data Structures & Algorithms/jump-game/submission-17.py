from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [None] * len(nums)
        return self.reachGoal(0, nums, memo)

    def reachGoal(self, i, nums, memo):
        if i >= len(nums) - 1:
            return True
        if memo[i] is not None:
            return memo[i]
        for step in range(nums[i], 0, -1):
            if self.reachGoal(i + step, nums, memo):
                memo[i] = True
                return True
        memo[i] = False
        return False