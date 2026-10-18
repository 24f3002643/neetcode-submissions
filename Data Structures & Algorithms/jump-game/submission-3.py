import sys
sys.setrecursionlimit(1000000)
# Brute Force
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.reachGoal(0, nums)
    
    def reachGoal(self,i, nums):
        if i >= len(nums)-1:
            return True
        curr_value = nums[i]
        while curr_value > 0:
            result = self.reachGoal(i + curr_value, nums)
            if result == False:
                curr_value -= 1
            else :
                return True
        return False

            
