# amount of water = width * height, width = distance between two selected lines, height => min height of two lines
# max amount of water, we need either a large width and min height, we need to check from the largest width
# as width decreases, a large amount needs a large min height

# Brute Force Example
"""
list   = [1, 8, 6, 2, 18, 4, 8, 3, 0, 18, 7]
width  = [0, 1, 2, 3, 4,  5, 6, 7, 8, 9, 10]
amount = [0, 1, 2, 3, 4,  5, 6, 7, 0, 9, 10]

list   = [8, 6, 2, 18, 4, 8, 3, 0, 18, 7]
width  = [0, 1, 2, 3,  4, 5, 6, 7, 8,  9]
amount = [0, 6, 4, 24,16,40,18, 0, 64,63]

list   = [6, 2, 18, 4, 8, 3, 0, 18, 7]
width  = [0, 1,  2, 3, 4, 5, 6,  7, 8]
amount = [0, 2, 12,12,24,15, 0, 42,48]

list   = [2, 18, 4, 8, 3, 0, 18, 7]
width  = [0,  1, 2, 3, 4, 5,  6, 7]
amount = [0,  2, 4, 6, 8, 0, 12,14]

list   = [18, 4, 8, 3, 0, 18, 7]
width  = [ 0, 1, 2, 3, 4,  5, 6]
amount = [ 0, 4,16, 9, 0, 90,42]

list   = [4, 8, 3, 0, 18, 7]
width  = [0, 1, 2, 3,  4, 5]
amount = [0, 4, 6, 0, 16,20]

"""

class Solution:
    # method signature, height is int list, output is int
    def maxArea(self, height: list[int]) -> int:

        right = len(height) - 1 
        left = 0
        max_amount = 0

        while left < right:

            # height = min(left line, right line)
            # width = right line - left line
            amount = (right - left) * min(height[left], height[right])

            if amount > max_amount:
                max_amount = amount

            # print(f"left: {left}, right: {right}, height: {min(height[left], height[right])}, amount: {max_amount}")

            if height[left] < height[right]:
                left += 1 # move left pointer
            else:
                right -= 1 # move right pointer

        return max_amount

container = Solution()
container.maxArea([1,8,6,2,5,4,8,3,7])