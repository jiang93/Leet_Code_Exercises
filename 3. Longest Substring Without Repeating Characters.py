from typing import Optional

# compare s[0] & s[1], compare s[0:1] & s[2], compare s[0:2] & s[3], ... until first string found again
# compare s[1] & s[2], compare s[1:2] & s[3], compare s[1:3] & s[4], ... unitl second string is found again
# continue until all s[-1] return the longest substring and length

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string_length = len(s)
        max_length = 0
        substring = None

        # if argument empty
        if not s:
            return 0
        
        # if argument contains only whitespace or only 1 character
        if s.isspace() or string_length == 1:
            return 1
        
        # check for longest substring 
        for start_id in range(string_length): # for s[0], s[1], s[2], s[4] ... 
            for stop_id in range(start_id+1, string_length): # for s[1], s[2], s[3], ...
                # if duplicated strings found in substring
                print(s[start_id:stop_id], s[stop_id])
                if (s[stop_id] in s[start_id:stop_id]): # if duplicated letters found
                    if (len(s[start_id:stop_id+1]) > max_length): 
                        substring = s[start_id:stop_id+1]
                        print(f"duplicated letters: {substring}")
                        max_length = len(substring)
                        break # exit the inner loop
                elif (s[stop_id] not in s[start_id:stop_id]): # if no duplicated letters
                    if (len(s[start_id:stop_id+1]) > max_length): 
                        substring = s[start_id:stop_id+1]
                        print(f"no duplicated letters: {substring}")
                        max_length = len(substring)
                
        return max_length
        # return f'The answer is "{substring}", with the length of {max_length}.'

s1 = Solution()
print(s1.lengthOfLongestSubstring("pwwkew")) # [(p,w), substring=pw, (pw, w), substring ]
# print(s1.lengthOfLongestSubstring("aabc"))
