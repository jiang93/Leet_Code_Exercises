# . => any characters except for newline 
# * => zero or more occurrences of the character
import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        x = re.fullmatch(p, s)
        if x:
            return True
        return False

match = Solution()
result = match.isMatch("aa", "a*")
print(result)
            
