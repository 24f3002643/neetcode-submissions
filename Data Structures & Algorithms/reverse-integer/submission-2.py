class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x = abs(x)
        
        if not negative :
            limit = pow(2, 31) - 1
        else :
            limit = pow(2, 31)
        quotient = limit // 10
        last_digit = limit % 10

        reverse = 0
        temp = x
        while temp > 0:
            rem = temp % 10
            if reverse == quotient:
                if rem > last_digit:
                    return 0
            elif reverse > quotient:
                    return 0
            reverse = reverse * 10 + rem
            temp = temp // 10
        
        if negative:
            reverse = (-1) * reverse
        
        return reverse