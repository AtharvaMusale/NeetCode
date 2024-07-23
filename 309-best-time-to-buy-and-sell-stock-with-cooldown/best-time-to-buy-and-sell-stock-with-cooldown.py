# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         # State: Buying or Selling?
#         # If Buy -> i + 1
#         # If Sell -> i + 2

#         dp ={}
#         def dfs(i,buying):
#             if i>= len(prices):
#                 return 0
            
#             if (i,buying) in dp:
#                 return dp[(i,buying)]
            
#             cooldown = dfs(i+1,buying)
#             if buying:
#                 buy = dfs(i+1, not buying) - prices[i]
#                 dp[(i,buying)] = max(buy,cooldown)
#             else:
#                 sell = dfs(i+2, not buying) +prices[i]
#                 dp[(i,buying)] = max(sell,cooldown)
#             return dp[(i,buying)]
#         return dfs(0,True)

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp_buy = [0] * n  # Max profit when buying
        dp_sell = [0] * n  # Max profit when selling

        dp_buy[0] = -prices[0]  # We buy on the first day

        for i in range(1, n):
            dp_buy[i] = max(dp_buy[i - 1], (dp_sell[i - 2] if i > 1 else 0) - prices[i])
            dp_sell[i] = max(dp_sell[i - 1], dp_buy[i - 1] + prices[i])

        return dp_sell[-1]

# Example usage
solution = Solution()
prices = [1, 2, 3, 0, 2]
print(solution.maxProfit(prices))  # Output: 3




#         # dp = {}  # key=(i, buying) val=max_profit

#         # def dfs(i, buying):
#         #     if i >= len(prices):
#         #         return 0
#         #     if (i, buying) in dp:
#         #         return dp[(i, buying)]

#         #     cooldown = dfs(i + 1, buying)
#         #     if buying:
#         #         buy = dfs(i + 1, not buying) - prices[i]
#         #         dp[(i, buying)] = max(buy, cooldown)
#         #     else:
#         #         sell = dfs(i + 2, not buying) + prices[i]
#         #         dp[(i, buying)] = max(sell, cooldown)
#         #     return dp[(i, buying)]

#         # return dfs(0, True)
