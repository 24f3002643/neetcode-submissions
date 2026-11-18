class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i
            diff = target - nums[i]
            if diff in dic:
                if i == dic[diff]:
                    continue
                return [dic[diff], i]

                
            

        