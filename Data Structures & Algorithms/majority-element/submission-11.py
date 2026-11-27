# Bit Manipulation
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        bits = [0 for i in range(32)]
        n = len(nums)
        
        for num in nums:
            for i in range(32):
                bits[i] += (num >> i) & 1
    
        
        res = 0
        for i in range(32):
            if bits[i] > n//2 :
                if i == 31:
                    res = res - (1 << i)
                else:
                    res = res | 1 << i

        return res