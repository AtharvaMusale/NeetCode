class Solution:

    def __init__(self, w: List[int]):
        self.cum_sum = []
        weight = 0
        for wt in w:
            weight += wt
            self.cum_sum.append(weight)


    def pickIndex(self) -> int:
        
        u = random.randint(1,self.cum_sum[-1])
        p = 0
        l,r  = 0, len(self.cum_sum)-1
        while l<=r:
            m = (l+r)//2
            if self.cum_sum[m]>=u:
                r = m -1 
                p = m
            else:
                l = m + 1
        return p

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()