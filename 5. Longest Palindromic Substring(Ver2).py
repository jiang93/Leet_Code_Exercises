# case 1: input string is empty
# case 2: input string has single character 
# case 3: input string is a palindrome 
# case 4: input string is a NOT palindrome

class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length <= 1:
            return s
        palindrome = str()

        for i in range(length):
            # odd length palindrome
            odd_padlindrome = self.isPalindrome(i, i, s) # s[i-1], s[i], s[i+1], compare s[i-1] and s[i+1]

            if len(odd_padlindrome) > len(palindrome):
                palindrome = odd_padlindrome

            # even length palindrome
            even_padlindrome = self.isPalindrome(i + 1, i, s) # compare s[i] and s[i+1], then s[i-1] and s[i+2] ... # s[i-1], s[i], s[i+1] => pass in s[i+1] shift left is s[i]

            if len(even_padlindrome) > len(palindrome):
                palindrome = even_padlindrome
                
        if not palindrome:
            palindrome = s[0]

        print(palindrome)
        return palindrome
        
    def isPalindrome(self, i: int, j: int, s: str) -> str:
        left = i - 1
        right = j + 1
        current_word = str()

        while left >= 0 and right < len(s) and s[left] == s[right]:
            # print(i, left, right, s[left:right+1])
            current_word = s[left:right+1]
            left -= 1
            right += 1

        return current_word

word = Solution()
word.longestPalindrome("baaaab")