
# class Solution:
#     def feasible(self, piles, h, k):
#         hours = 0
#         for p in piles:
#             hours += math.ceil(p/k)
#             return hours <= h


#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         low, high = 1, len(piles)
#         ans = -1
#         while low<=high:
#             mid = (low+high)//2
#             if self.feasible(piles, h, mid):
#                 ans = mid
#                 high = mid-1
#             else:
#                 low = mid + 1
#         return ans

class Solution:
    def feasible(self, piles, h, k):
        hours = 0
        for p in piles:
            hours += math.ceil(p / k)
        return hours <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        ans = -1
        while low<=high:
            mid = (low+high)//2
            if self.feasible(piles, h, mid):
                ans = mid
                high = mid-1
            else:
                low = mid + 1

        return ans
                