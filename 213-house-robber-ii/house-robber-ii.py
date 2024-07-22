class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        
        def robFrom(nums):
            dp = [0] * len(nums)
            dp[0], dp[1] = nums[0], max(nums[0], nums[1])
            for i in range(2,len(nums)):
                dp[i] = max(dp[i-1], nums[i]+dp[i-2])
            return dp[-1]
        
        return max(robFrom(nums[1:]), robFrom(nums[:-1]))




























        # if len(nums) <= 2: return max(nums) 
        # def rob(nums):
        #     n = len(nums)
        #     dp= [0] * len(nums)
        #     dp[0], dp[1] = nums[0],  max(nums[0], nums[1])
        #     for i in range(2, n):
        #         dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        #     return dp[-1]
        # return max(rob(nums[1:]), rob(nums[:-1]))
      