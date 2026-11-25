# Messy Optimized Code
# Optimized Code
# Two Pointer
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)

        if n==1 and nums[0] == val:
            return 0
        start = 0
        end = n-1
        count = 0

        while start <= end and count != n:
            print(count)
            if nums[start] == val:
                while  start < end and nums[end] == val:
                    end -= 1
                    count += 1
                nums[start], nums[end] = nums[end], nums[start]
                count += 1
                end -= 1
            start += 1
        
        return n-count
                

# Clean Optimized Code
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
                

        
