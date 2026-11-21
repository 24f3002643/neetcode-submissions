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
            lcp.clear()
            lcp = list(prefix)
        return "".join(lcp)