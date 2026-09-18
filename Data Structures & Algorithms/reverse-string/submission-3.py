class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Brute Force Method
        l = []
        for i in s[::-1]:
            l.append(i)
        for i in range(len(s)):
            s[i] = l[i]
        return None