class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []

        curr_sum = 0
        for i in range(len(w)):
            curr_sum += w[i]
            self.prefix_sum.append(curr_sum)

        self.total_sum = curr_sum
        
    def pickIndex(self) -> int:
        target = random.randint(1, (self.total_sum))

        l, r = 0, len(self.prefix_sum)-1

        while l<r:
            m = (l+r)//2
            if self.prefix_sum[m] >= target:
                r = m
            else:
                l = m +1
        
        return l
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()