# Brute Force
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        lst = []

        for i in nums:
            if i != val:
                lst.append(i)
        
        for i in range(len(lst)):
            nums[i] = lst[i]
        
        return len(lst)

