# int is a palindrome (odd digits palindrome 121, or even digits padlindrome 2442)
# int is NOT a palindrome (single digit, negative number)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            divisor = 1
            reverse = int()

            while x//divisor > 0:
                digit = x // divisor % 10
                reverse = reverse * 10 + digit
                divisor *= 10
                print(digit, reverse)

        return x==reverse
        """
        """ simple solution """
        num_string = str(x)
        
        if num_string == num_string[::-1]:
            return True
        return False

num = Solution()
num.isPalindrome(121)
        