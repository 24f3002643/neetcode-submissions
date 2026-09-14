class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ''' 
        # Brute Force Approach
        index=[0,0]
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target :
                    index[0], index[1] = [i+1,j+1]
                    break
        return index
        '''

        # Optimized Approach
        index = [0,0]
        i=0
        j = len(numbers)-1
        while (i<j):
            if numbers[i] + numbers[j] == target:
                index[0], index[1] = [i+1, j+1]
                break
            elif numbers[i] + numbers[j] < target :
                i += 1
            else :
                j -= 1
        return index
