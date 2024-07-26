# class Solution:
#     def sortArrayByParity(self, nums: List[int]) -> List[int]:
#         l, r = 0, len(nums)-1
#         while l<r:
#             if nums[l]%2 > nums[r]%2==1:
#                 nums[r], nums[l] = nums[l], nums[r]

#             if nums[l]%2 == 0:
#                 l+=1
#             if nums[r]%2 ==0:
#                 r-=1
#             # elif nums[l]%2==0:
#             #     l+=1
#         return nums

from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] % 2 > nums[r] % 2:
                nums[l], nums[r] = nums[r], nums[l]

            if nums[l] % 2 == 0:
                l += 1
            if nums[r] % 2 == 1:
                r -= 1
                
        return nums

