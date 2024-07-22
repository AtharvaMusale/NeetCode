# class Solution:
#     def rob(self, nums: List[int]) -> int:
        # rob1, rob2 = 0,0
        # # [rob1,rob2,n,n+1,n+2,....]
        # for n in nums:  
        #     tmp = max(n + rob1,rob2)
        #     rob1 = rob2
        #     rob2 = tmp
        # return rob2


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums)==1:
            return nums[0]
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]

        # memo = {}
        # def robFrom(i):
        #     if i>=len(nums):
        #         return 0

        #     if i in memo:
        #         return memo[i]

        #     memo[i] = max(nums[i] + robFrom(i+2), robFrom(i+1))    
        #     return memo[i]
        
        # return robFrom(0)