class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if set(s) != set(t):
            return False
        dic1 = {}
        dic2 = {}
        for i in s:
            if i not in dic1:
                dic1[i] = 0
            dic1[i] += 1
        print(dic1)
        for j in t:
            if j not in dic2:
                dic2[j] = 0
            dic2[j] += 1
        print(dic2)
        for i in dic1:
            print(i, dic1[i], dic2[i])
            if dic1[i] != dic2[j]:
                return False
        return True   
        