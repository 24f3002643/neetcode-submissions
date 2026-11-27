# Brute Force
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            count = 1
            for j in range(i+1,n):
                if nums[i] == nums[j]:
                    count += 1
            if count >= (n//2):
                return nums[i]
