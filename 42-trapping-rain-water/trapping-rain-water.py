# class Solution:
#     def trap(self, nums: List[int]) -> int:
#         # res = 0
#         # l, r = 0, len(nums)-1
#         # leftMax, rightMax = nums[l], nums[r]

#         # while l<r:
#         #     if leftMax<rightMax:
#         #         l+=1
#         #         leftMax = max(leftMax,nums[l])
#         #         res += leftMax- nums[l]

#         #     else:
#         #         r-=1
#         #         rightMax = max(rightMax, nums[r])
#         #         res += rightMax- nums[r]

#         # return res 

#         res = 0
#         l, r = 0, len(nums)-1
#         leftMax, rightMax = nums[l], nums[r]

#         while l<r:
#             if leftMax<rightMax:
#                 l+=1
#                 leftMax = max(leftMax, nums[l])
#                 res += leftMax- nums[l]
            
#             else:
#                 r-=1
#                 rightMax = max(rightMax, nums[r])
#                 res+= rightMax - nums[r]
#         return res

class Solution:
    def trap(self, nums: List[int]) -> int:
        # Edge case: If the list has fewer than 3 elements, no water can be trapped
        if len(nums) < 3:
            return 0

        res = 0
        l, r = 0, len(nums) - 1
        left_max, right_max = nums[l], nums[r]

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, nums[l])
                res += left_max - nums[l]  # Add water trapped at index l
            else:
                r -= 1
                right_max = max(right_max, nums[r])
                res += right_max - nums[r]  # Add water trapped at index r

        return res
