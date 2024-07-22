# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [amount+1] * (amount+1)
#         dp[0] = 0

#         for a in range(amount+1):
#             for c in coins:
#                 if a-c >=0:
#                     dp[a] = min(dp[a], 1 + dp[a-c])
        
#         return dp[amount] if dp[amount]!= amount+1 else -1


from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Dictionary to store the minimum coins needed for each amount
        memo = {}
        
        def dp(n):
            # Base cases
            if n == 0:
                return 0
            if n < 0:
                return float('inf')
            
            # If result is already computed, return it
            if n in memo:
                return memo[n]
            
            # Initialize the minimum coins needed to a large number
            min_coins = float('inf')
            for coin in coins:
                res = dp(n - coin)
                if res != float('inf'):
                    min_coins = min(min_coins, res + 1)
            
            # Store the computed result in memo
            memo[n] = min_coins
            return min_coins
        
        result = dp(amount)
        return result if result != float('inf') else -1
