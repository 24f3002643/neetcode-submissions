class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        
        for i in strs:
            array = [0] * n
            for j in i:
                print(j)
                array[ord(j) - ord('a')] += 1
            if tuple(array) not in dic:
                dic[tuple(array)] = []
            dic[tuple(array)].append(i)
        
        return list(dic.values())
        