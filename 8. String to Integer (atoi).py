# step 1: read leading whitespace
# step 2: read + or - sign
# step 3: read number until next charater is a non-digit, leading 0 is ignored
# # cannot use int() function
class Solution:
    def myAtoi(self, s: str) -> int:

        s_num = str()
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        sign = 1
        if s[0].isspace: # remove leading space
            s = s.lstrip() 

        if s[0] == "-": # remove -/+ sign 
            sign = -1
            s = s.lstrip("-")
        else:
             s = s.lstrip("+")

        for i in s:
            if i in numbers:
                s = s.lstrip("0")
                s_num += i
            else:
                break

        s_num = int(s_num)
        num = sign*s_num

        if num < -2**31:
            num = -2**31

        if num > 2**31-1:
            num = 2**31-1

        print(num)
        return num

string_num = Solution()
string_num.myAtoi("1337c0d3")