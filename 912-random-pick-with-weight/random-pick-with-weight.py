class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []

        total = 0
        for i in w:
            total+=i
            self.prefix_sum.append(total)
        self.total = total


    def pickIndex(self) -> int:
        l, r = 0, len(self.prefix_sum) -1
        target = random.randint(1, self.total)

        while l<r:
            m = (l + r)//2
            if self.prefix_sum[m]<target:
                l = m + 1
            else:
                r = m
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()