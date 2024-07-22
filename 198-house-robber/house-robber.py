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
            # Base case: No houses left to rob
            if i >= len(nums):
                return 0
            # If result is already computed, return it
            if i in memo:
                return memo[i]
            
            # Recurrence relation: rob the current house and move to the house after the next one,
            # or skip the current house and move to the next house
            rob_current = nums[i] + robFrom(i + 2)
            skip_current = robFrom(i + 1)
            memo[i] = max(rob_current, skip_current)
            return memo[i]
        
        return robFrom(0)
