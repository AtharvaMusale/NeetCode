from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Remove duplicates
        nums = list(set(nums))
        
        # Sort the list in descending order
        nums.sort(reverse=True)
        
        # If there are at least 3 unique elements, return the third maximum
        if len(nums) >= 3:
            return nums[2]
        
        # Otherwise, return the maximum element
        return nums[0]

