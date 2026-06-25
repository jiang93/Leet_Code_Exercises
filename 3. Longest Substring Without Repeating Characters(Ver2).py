from typing import Optional

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string_length = len(s)
        substring = None
        start_idx = 0
        max_length = 0
        seen = {}

        # if argument is empty
        if not s:
            return 0
        
        # if argument contains only whitespace or only 1 character
        if s.isspace() or string_length == 1:
            return 1
        
        # check for longest substring 
        for idx in range(string_length): # idx = 0, 1, 2, 3, 4 ...
            char = s[idx]
            # print(idx, char)

            # if duplicated characters found in string 
            if char in seen:
                if (len(s[start_idx:idx]) > max_length): # replace substring with current substring if it is longer 
                    substring = s[start_idx:idx]
                    max_length = len(substring)

                if (seen[char] + 1 > start_idx): # if previous seen char location is after the current start_idx, update the start_idx
                    start_idx = seen[char] + 1

            seen[char] = idx # save character and number of occurence into key-pairs
        
        # if no duplicated characters found in string
        if (len(s[start_idx:idx+1]) > max_length):
            substring = s[start_idx:idx+1]
            max_length = len(substring)
        
        print(substring)
        return max_length
        # return f'The answer is "{substring}", with the length of {max_length}.'

s1 = Solution()
s1.lengthOfLongestSubstring("pwwkew")
#s1.lengthOfLongestSubstring("dvdkew")
s1.lengthOfLongestSubstring("abba")
#s1.lengthOfLongestSubstring("abcdee")
#s1.lengthOfLongestSubstring("adbecdefe")
#s1.lengthOfLongestSubstring("au")


