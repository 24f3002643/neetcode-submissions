# Brute Force Approach
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = []
        selected_str = strs[0]
        for i in range(1, len(selected_str)+1):
            prefix = selected_str[:i] 
            for j in strs[1:]:
                if i == len(j)+1 or prefix != j[:i]:
                    return "".join(lcp)
            lcp = list(prefix)
        return "".join(lcp)
        # For each iteration of outer loop, O(n*i) work is done, since for each of n words, O(i) is used for slicing of string j.
        # Now summing over for all i, n*1 + n*2 + n*3 + ... + n*p = n*p*(p+1)/2
        
