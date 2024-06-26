class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res = [0] * (len(cost) + 1)

        for i in range(2,len(cost)+1):
            take_one_step = res[i-1] + cost[i-1]    
            take_two_steps = res[i-2] + cost[i-2]
            res[i] = min(take_one_step,take_two_steps)
        
        return res[-1]