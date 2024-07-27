# class Solution:
#     def buyChoco(self, prices: List[int], money: int) -> int:
#         prices.sort()
#         if prices[0]+prices[1]>money:
#             return money
#         else:
#             return money - (prices[0]+prices[1])
        
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        min_cost = prices[0] + prices[1]

        if min_cost <= money:
            return money - min_cost
        return money