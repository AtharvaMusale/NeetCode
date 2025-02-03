# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
#         l = 0
#         ans = 0
#         zeros = 0
#         ones = 0

#         for r in range(len(nums)):
#             if nums[r] == 0:
#                 zeros+=1
#             else:
#                 ones+=1
            
#             while zeros>k:
#                 if nums[l] == 0:
#                     zeros-=1
#                 else:
#                     ones-=1
#                 l+=1
#             ans = max(ans, r-l+1)
#         return ans

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] == 0:
                k -= 1
            j += 1
            if k < 0:
                if nums[i] == 0:
                    k += 1
                i += 1
        return j - i