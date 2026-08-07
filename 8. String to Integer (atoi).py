# step 1: read leading whitespace
# step 2: read + or - sign
# step 3: read number until next charater is a non-digit, leading 0 is ignored
# # cannot use int() function

class Solution:
    def myAtoi(self, s: str) -> int:
        string_num = 0
        sign = 1

        if not s:
            return 0
        
        if s[0].isspace: # remove leading space
            s = s.lstrip()

        if s and s[0] == "-": # remove -/+ sign 
            sign = -1
            s = s.removeprefix("-")
        else:
             s = s.removeprefix("+")

        for i in s:
            if i.isdigit():
                # ord(i) converts the character into ascii code value
                string_num = string_num*10 + (ord(i)-48)
                # print(ord(i)) 
            else:
                break

        string_num *= sign

        if string_num < -2**31:
            string_num = -2**31

        if string_num > 2**31-1:
            string_num = 2**31-1

        print(string_num)
        return string_num


string_num = Solution()
string_num.myAtoi("1337c0d3")