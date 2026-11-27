# Bit Manipulation
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        bits = [0 for i in range(32)]
        n = len(nums)
        
        for num in nums:
            for i in range(32):
                bits[i] += (num >> i) & 1
                # right shift operation
                # >> brings out the ith bit out
        # one important thing to note here is that we are just counting bit 1, and not bit 0.
        # bits array only the count the bit 1 at ith bit position across all numbers.
        # This works because all the 32 bits of res are 0. So we need to set only bit 1 at their respective position in res.
        # Had res had any other number/character other than 0 or 1. Then we would have needed count of both 0 and 1 at ith bit position.
        
        res = 0
        for i in range(32):
            if bits[i] > n//2 :
                if i == 31:
                    res = res - (1 << i)
                    # (1 << i) shift 1 to i bit left
                    # this subtraction is to handle negative numbers whose MSB is -1.
                else:
                    res = res | 1 << i
                    # | operation puts ith bit to 1

        return res
