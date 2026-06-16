class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # lenght of list
        list_len = len(nums)
        # i = 0, 1, 2, ..., list_len
        for i in range(list_len):
            # j = 1, 2, ..., list_len
            for j in range(i + 1, list_len):
                # check if sum = target
                if nums[i] + nums[j] == target:
                    return [i, j]

print(Solution().twoSum([1, 8, 3, 4, 5], 8))