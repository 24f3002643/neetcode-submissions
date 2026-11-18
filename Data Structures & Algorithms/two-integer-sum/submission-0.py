class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[i] = i
            if (target-nums[i]) in dic:
                return [dic[i], dic[target-nums[i]]]

        