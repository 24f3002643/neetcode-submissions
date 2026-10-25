class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x = abs(x)
        
        reverse = 0
        temp = x
        while temp > 0:
            rem = temp % 10
            reverse = reverse * 10 + rem
            temp = temp // 10
        
        if negative:
            reverse = (-1) * reverse
        
        lower = (-1) * pow(2, 31)
        upper = pow(2, 31) - 1

        if lower <= reverse <= upper:
            return reverse
        else:
            return 0