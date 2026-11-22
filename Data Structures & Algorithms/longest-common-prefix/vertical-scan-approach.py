# Vertical Scan Approach
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = []
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if i >= len(strs[j]):
                    return "".join(lcp)
                if strs[0][i] != strs[j][i]:
                    return "".join(lcp)
            lcp.append(strs[0][i])
        return "".join(lcp)
