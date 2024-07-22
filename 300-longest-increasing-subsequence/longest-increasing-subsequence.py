class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1]* len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    lis[i] = max(lis[i],1+lis[j])
        return max(lis)
        # n = len(nums)
        # dp = [[0] * (n+1)]*(n+1)
        # for i in range(n-1,-1,-1):
        #     for j in range(n-1,-2,-1):
        #         ans = dp[i+1][j+1]
        #         if j == -1 or nums[i] > nums[j]:
        #             ans = max(ans, dp[i+1][i+1]+1)
        #         dp[i][j] = ans
        # print(dp)

        # return dp[0][0]