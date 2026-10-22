class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic1 = {}
        dic2 = {}
        for i in s:
            if i not in dic1:
                dic1[i] = 0
            dic1[i] += 1
        for j in t:
            if j not in dic2:
                dic2[j] = 0
            dic2[j] += 1
        for i in dic1:
            if dic1[i] != dic2[i]:
                return False
        return True   
        