# Brute Force 2 - Method 2
# Sorting, and Comparing against each other
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str = []

        for i in strs:
            sorted_str.append("".join(sorted(i)))

        anagram_list = []
        n = len(sorted_str)
        marked = [0 for i in range(n)] 
        for i in range(n):
            if marked[i] == 1:
                continue
            lst = []
            lst.append(strs[i])
            marked[i] = 1
            
            for j in range(i+1, n):
                if marked[j] == 1:
                    continue
                if sorted_str[i] == sorted_str[j]:
                    lst.append(strs[j])
                    marked[j] = 1
            
            anagram_list.append(lst.copy())
        
        return anagram_list
