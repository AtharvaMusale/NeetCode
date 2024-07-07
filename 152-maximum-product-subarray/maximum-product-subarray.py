class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMin, currMax = 1,1

        for i in nums:
            tmp = i * currMax
            currMax = max(i * currMax, i * currMin, i)
            currMin = min(tmp, i * currMin, i)
            res = max(res,currMax)
        
        return res