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
        memo = {}
        def robFrom(i):
            if i>=len(nums):
                return 0

            if i in memo:
                return memo[i]

            memo[i] = max(nums[i] + robFrom(i+2), robFrom(i+1))    
            return memo[i]
        
        return robFrom(0)