from typing import Optional

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string_length = len(s)
        substring = None
        max_length = 0
        seen = {}

        # if argument empty
        if not s:
            return 0
        
        # if argument contains only whitespace or only 1 character
        if s.isspace() or string_length == 1:
            return 1
        
        # check for longest substring 
        for idx in range(string_length): # idx = 0, 1, 2, 3, 4 ...
            char = s[idx]
            seen[char] = idx
            substring = seen[left:idx]

        print(seen)
        return max_length
        # return f'The answer is "{substring}", with the length of {max_length}.'

s1 = Solution()
s1.lengthOfLongestSubstring("pwwkew") # [(p,w), substring=pw, (pw, w), substring ]
s1.lengthOfLongestSubstring("aabc")
s1.lengthOfLongestSubstring("abcdee")
s1.lengthOfLongestSubstring("abcdefe")

