class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        i=0
        while i <= n-1:
            if nums[i] == 0:
                break
            i = i + nums[i]

        if i >= n-1:
            return True
        else:
            return False
        