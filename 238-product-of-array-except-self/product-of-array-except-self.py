# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         # res = [1] * (len(nums))

#         # for i in range(1, len(nums)):
#         #     res[i] = res[i-1] * nums[i-1]
#         # postfix = 1
#         # for i in range(len(nums) - 1, -1, -1):
#         #     res[i] *= postfix
#         #     postfix *= nums[i]
#         # return res
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # Left products
        left_product = 1
        for i in range(n):
            output[i] = left_product
            left_product *= nums[i]

        # Right products
        right_product = 1
        for i in range(n-1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]

        return output