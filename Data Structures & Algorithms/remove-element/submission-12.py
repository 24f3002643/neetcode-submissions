# Optimized Code
# Two Pointer
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)

        start = 0
        end = n-1

        while start <= end :
            if nums[start] == val:
                while start < end and nums[end] == val:
                    end -= 1
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
                start += 1
            else:
                start += 1
        return end+1
                

        