# Optimized code
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        result = [0] * n
        n = len(temperatures)
        for i in range(n):
            if not stack:
                stack.append((i,temperatures[i]))
            while stack and temperatures[i] > stack[-1][1]:
                result[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append((i, temperatures[i]))
        return result

        