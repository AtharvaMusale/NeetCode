class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = [1] * len(nums)

        # i = 1
        # while i<len(nums):
        #     res[i] = nums[i-1] * res[i-1]
        #     i+=1

        # prod = 1
        # i = len(nums)-2
        # while i >= 0:
        #     prod *= nums[i+1]
        #     res[i] *= prod
        #     i-=1
        # return res


        res = [1]* len(nums)
        i = 1
        while i < len(nums):
            res[i] = res[i-1] * nums[i-1]
            i+=1

        i = len(nums)-2
        prod = 1
        while i>=0:
            prod *= nums[i+1]
            res[i] *= prod
            i-=1
        return res

