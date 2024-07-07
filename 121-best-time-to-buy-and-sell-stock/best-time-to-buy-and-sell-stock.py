class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        curr_profit = 0
        max_profit = 0
        min_value = float("inf")

        for i in range(len(prices)):
            if prices[i] < min_value:
                min_value = prices[i]
            
            if prices[i] - min_value > max_profit:
                curr_profit = prices[i] - min_value
            
            max_profit = max(curr_profit, max_profit)
        
        return max_profit


        # if not prices:
        #     return 0
        
        # curr_profit = 0
        # max_profit = 0
        # min_value = float("inf")

        # for i in range(len(prices)):
        #     if prices[i]<min_value:
        #         min_value = prices[i]
        #     if prices[i]-min_value > max_profit:
        #         curr_profit = prices[i]-min_value
            
        #     max_profit = max(max_profit, curr_profit)

        # return max_profit
        



# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:

#         if not prices:
#             return 0
        
#         min_val = float("inf")
#         profit = 0
#         curr_profit = 0
#         for i in range(len(prices)):
#             if prices[i] < min_val:
#                 min_val = prices[i]
            
#             if prices[i] - min_val > profit:
#                 curr_profit = prices[i] - min_val
            
#             profit = max(profit,curr_profit)
#         return profit


