#     P A Y P A L I S H I  R I  N  G
# idx 0 1 2 3 4 5 6 7 8 9 10 11 12 13


# P      A        H        N  
#  A   P   L   S    I   I    G
#    Y       I        R 

# idx 0 1 2 3 4 5 6 7 8 9 10 11 12 13
# pos 0 1 2 3 0 1 2 3 0 1  2  3  0  1  (4 postions per cycle)
# row 0 1 2 1 0 1 2 1 0 1  2  1  0  1

# P             I              N  
#  A         L    S         I    G
#    Y    A         H     R 
#      P               I

# idx 0 1 2 3 4 5 6 7 8 9 10 11 12 13
# pos 0 1 2 3 4 5 0 1 2 3  4  5  0  (6 positions per cycle)
# row 0 1 2 3 2 1 0 1 2 3  2  1  0

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        length = len(s)
        if length <= numRows or numRows <= 1:
            return s
        
        output_s = str()
        current_row = 0
        idx = 0
        cycle = numRows * 2 - 2

        # row = 0, 1, 2 ... numRows
        while current_row < numRows:

            # if hitting the maximum idx of the current, go to next row
            if idx >= length:
                current_row += 1
                idx = 0

            # check the position 
            pos = idx % cycle

            # check the row based on idx
            if pos < numRows:
                idx_row = pos
            else:
                idx_row = cycle - pos

            #print(current_row, idx, pos, idx_row)
            # if it belongs to current_row 
            if (idx_row == current_row):
                output_s += s[idx]

            idx += 1

        print(output_s)
        return output_s

word = Solution()
word.convert("PAYPALISHIRING", 3)