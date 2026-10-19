# Brute Force with memoization
import sys
sys.setrecursionlimit(1000000)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [None] * len(nums)
        return self.reachGoal(0, nums, memo)
    '''
    def reachGoal(self,i, nums, memo):
        if memo[i] is not None:
            return memo[i]
        if i >= len(nums)-1:
            memo[-1] = True
            return True
        curr_value = nums[i]
        while curr_value > 0:
            if  i + curr_value <= len(nums) -1 :
                if memo[i + curr_value] == True:
                    memo[i] = True
                    return True
                else :
                    result = self.reachGoal(i + curr_value, nums, memo)
                    if result:
                        memo[i] = True
                        return True
            curr_value -= 1
        memo[i] = False
        return False
    '''
    def reachGoal(self,i, nums, memo):
        if i >= len(nums)-1:
            return True
        if memo[i] is not None:
            return memo[i]
        for step in range(nums[i], 0, -1):
            if self.reachGoal(i+step, nums, memo):
                memo[i] = True
                return True
            memo[i] = False
            return False