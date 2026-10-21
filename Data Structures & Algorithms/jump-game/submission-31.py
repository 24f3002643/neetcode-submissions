# Forward Pass Greedy Approach
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0
        for i in range(0, len(nums)):
            if max_index >= len(nums)-1:
                return True
            if nums[i] == 0 and max_index <= i:
                return False
            if nums[i]+i > max_index:
                max_index = nums[i] + i
