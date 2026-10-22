class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s= s.lower()
        t = t.lower()
        if len(s) != len(t):
            return False
        arr = [0] * 26

        for i in s:
            arr[ord(i) - ord('a')] +=1
        
        for j in t:
            arr[ord(j) - ord('a')] -= 1
        
        for i in arr:
            if i != 0:
                return False
        return True
        