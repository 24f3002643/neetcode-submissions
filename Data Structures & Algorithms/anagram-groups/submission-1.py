class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_list = []
        n = len(strs)
        marked = [0] * n
        lst = []
        for i in range(n):
            if marked[i] == 1:
                continue
            lst.append(strs[i])
            marked[i] = 1
            for j in range(i+1, n):
                if marked[j] == 1:
                    continue
                if self.isAnagram(strs[i], strs[j]):
                    lst.append(strs[j])
                    marked[j] = 1
            if lst:
                anagram_list.append(list(lst))
                lst.clear()
        return anagram_list


    
    def isAnagram(self, s, t):
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
        