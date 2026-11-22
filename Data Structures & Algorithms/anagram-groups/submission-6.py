# Naive Solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for i in strs:
            sorted_str = "".join(sorted(i))
            if sorted_str not in dic:
                dic[sorted_str] = []
            dic[sorted_str].append(i)
        
        return list(dic.values())

        