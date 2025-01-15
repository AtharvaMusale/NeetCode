class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Return profit
        # Can there be negative prices? No
        #  Duplicates? Maybe
        
        # Approach:
        # [7,1,5,3,6,4] : l=3,r=6 profit = 7
        maxP = 0
        l,r = 0,1
        while r<len(prices):
            if prices[l]<prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(profit,maxP)
            else:
                l = r
            r +=1
        return maxP
