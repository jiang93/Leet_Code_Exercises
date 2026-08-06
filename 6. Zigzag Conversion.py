# P A Y P A L I S H I  R I  N  G
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13
# 0 1 2 1 0 1 2 1 0 1  2  1  0  1

# 0 1 2 3 2 1 0 1 2 3  2  1  0  1
# 0 1 2 3 4 3 2 1 0 1  2  3  4  3

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        length = len(s)
        if length <= numRows:
            return s
        
        output_s = str()
        row = 0
        idx = 0
        cycle = numRows * 2 - 2

        # row = 0, 1, 2 ... numRows
        while row < numRows:
            if idx >= length:
                row += 1
                idx = 0
            print(idx // cycle)
            idx += 1

        print(output_s)

word = Solution()
word.convert("PAYPALISHIRING", 3)