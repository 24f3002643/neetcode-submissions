class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        dic = {}
        for i in strs:
            array = [0] * 26
            for j in i:
                array[ord(j) - ord('a')] += 1
            if tuple(array) not in dic:
                dic[tuple(array)] = []
            dic[tuple(array)].append(i)
        
        return list(dic.values())
        