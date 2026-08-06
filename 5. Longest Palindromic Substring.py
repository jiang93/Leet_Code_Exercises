# case 1: input string is empty
# case 2: input string has single character 
# case 3: input string is a palindrome 
# case 4: input string is a NOT palindrome

class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        palindrome = str()
        if length <= 1:
            return s
        
        for start_idx in range(length):
            for stop_idx in range(start_idx + 1, length):

                if (s[start_idx] == s[stop_idx]):
                    # print(s[start_idx:stop_idx+1])
                    current_length = stop_idx - start_idx + 1

                    if current_length > len(palindrome):
                        mid_idx = (start_idx + stop_idx) // 2

                        if current_length % 2 == 0: # if index is even
                            #print(f"{start_idx}, {stop_idx}, {mid_idx}, forward: {s[start_idx:mid_idx+1]}, backward: {s[mid_idx+1:stop_idx+1][::-1]}")

                            if (s[start_idx:mid_idx+1] == s[mid_idx+1:stop_idx+1][::-1]):
                                palindrome = s[start_idx:stop_idx+1]
                        else:
                            #print(f"{start_idx}, {stop_idx}, {mid_idx}, forward: {s[start_idx:mid_idx+1]}, backward: {s[mid_idx:stop_idx+1][::-1]}")

                            if (s[start_idx:mid_idx+1] == s[mid_idx:stop_idx+1][::-1]):
                                palindrome = s[start_idx:stop_idx+1]
                    """ creating a new string by slicing substring and reversing it consumes more time and memory
                    current_word = s[start_idx:stop_idx+1]
                    print(f"{start_idx}, {stop_idx}, read forward: {current_word}, read backward: {current_word[::-1]}")
                    # check whether the substring is a palindrome, and if it is the longest palindrome
                    if (current_word == current_word[::-1] and len(current_word) > len(palindrome)):
                        palindrome = current_word
                    """

        if not palindrome:
            palindrome = s[0]
            
        print(palindrome)
        return palindrome

word = Solution()
word.longestPalindrome("abcba")