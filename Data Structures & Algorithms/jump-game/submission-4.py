# Brute Force without memoization
import sys
sys.setrecursionlimit(1000000)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.reachGoal(0, nums)
    
    def reachGoal(self,i, nums):
        if i >= len(nums)-1:
            return True
        curr_value = nums[i]
        while curr_value > 0:
            result = self.reachGoal(i + curr_value, nums)
            if result:
                return True
            else:
                curr_value -= 1
        return False

            
