# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:

#         max_sum = 0
#         curr_sum = 0 
#         for n in nums:
#             curr_sum += n
#             max_sum = max(max_sum, curr_sum)
#             if curr_sum < 0:
#                 curr_sum = 0
#         return max_sum
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]  # Initialize max sum
        current_sum = 0  # Current running sum
        
        for num in nums:
            current_sum += num  # Add current number to subarray sum
            max_sum = max(max_sum, current_sum)  # Update max sum if needed
            if current_sum < 0:  # If sum becomes negative, reset it
                current_sum = 0
        
        return max_sum
