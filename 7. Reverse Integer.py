# signed 32-bit integer => -2^31 to +(2^31 - 1)
# -2,147,483,648 to +2,147,483,647

class Solution:
    def reverse(self, x: int) -> int:
        divisor = 1
        digits = []
        number = int()
        sign = 1

        if x < 0:
            sign = -1
            x = abs(x)

        while (x // divisor) > 0:
            digit = x//divisor % 10
            digits.append(digit)
            divisor *= 10

        for i in digits:
            divisor //= 10
            number += i*divisor

        if -2**31 <= sign*number < 2**31:
            # print(sign*number)
            return sign*number
        else:
            return 0

num = Solution()
num.reverse(-9034)