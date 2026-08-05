class Solution:
    # findMedianSortedArrays(self, nums1, nums2) where nums1 and nums2 are 2 sorted list
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        median = None
        len_s1 = len(nums1)
        len_s2 = len(nums2)
        len_total = len_s1 + len_s2
        # if both list is empty
        if len_total == 0:
            return median

        previous_num = None
        current_num = None
  
        idx_s1 = 0
        idx_s2 = 0

        middle_idx = len_total // 2

        for _ in range(middle_idx+1):
            previous_num = current_num # update previous number
            if idx_s1 >= len_s1: # if current idx exceed list length
                current_num = nums2[idx_s2]
                idx_s2 += 1
            elif idx_s2 >= len_s2:
                current_num = nums1[idx_s1]
                idx_s1 += 1
            elif nums1[idx_s1] < nums2[idx_s2]: # if list value is smaller 
                current_num = nums1[idx_s1]
                idx_s1 += 1
            else:
                current_num = nums2[idx_s2]
                idx_s2 += 1

        if len_total % 2 == 0:
            median = (previous_num + current_num) / 2
        else:
            median = current_num
        return round(median, 1)
        
list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]
median = Solution()
print(median.findMedianSortedArrays(list_a, list_b))