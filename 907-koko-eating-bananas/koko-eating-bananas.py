class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check_feasibility(piles, k, h):
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            return hours<= h
        
        l,r = 1, max(piles)

        while l<=r:
            k = l + ((r-l)//2)
            if check_feasibility(piles,k,h):
                r = k -1

            else:
                l = k + 1
                
        return l