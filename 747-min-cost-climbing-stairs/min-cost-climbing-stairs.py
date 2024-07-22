class Solution:
    def minCostClimbingStairs(self, arr: List[int]) -> int:
        # for i in range(len(nums)-3,-1,-1):
        #     nums[i] += min(nums[i+1] , nums[i+2])

        # return min(nums[0],nums[1])     
        memo = {}
        def recur(i):
            if i>=len(arr):
                return 0
            if i in memo:
                return memo[i]
            
            cost = arr[i] + min(recur(i+1) , recur(i+2))

            memo[i] = cost
            return cost
        
        return min(recur(0),recur(1))
        
            


















        # for i in range(len(cost)-3,-1,-1):
        #     cost[i] += min(cost[i+1],cost[i+2])
        
        # return min(cost[0],cost[1])