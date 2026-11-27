# Randomization
import random
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        iter = 0

        while(True):
            iter += 1
            count = 0
            candidate = random.choice(nums)
            for i in nums:
                if i==candidate:
                    count += 1
            if count > (n//2):
                print(f"Total iter required : {iter}")
                return candidate
