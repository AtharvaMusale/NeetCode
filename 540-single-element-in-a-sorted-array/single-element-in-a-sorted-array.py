from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        while l < h:
            m = l + (h - l) // 2
            # Ensure m is even
            if m % 2 == 1:
                m -= 1
            # If the pair starts at m is equal, the single element is on the right side
            if nums[m] == nums[m + 1]:
                l = m + 2
            else:
                h = m
        return nums[l]
