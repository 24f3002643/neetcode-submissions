class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index=[0,0]
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target :
                    index[0], index[1] = [i+1,j+1]
                    break
        return index