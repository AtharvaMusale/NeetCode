class Solution:
    def check_feasibile(self, piles, k, h):
        hours = 0
        for p in piles:
            hours += math.ceil(p/k)
        return hours<=h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        ans = -1
        while l<=r:
            k = l + ((r-l)//2)
            if self.check_feasibile(piles, k, h):
                ans = k
                r = k-1

            else:
                l = k + 1
        
        return ans