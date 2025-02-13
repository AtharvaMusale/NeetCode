class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.blacklist_set = set(blacklist)
        self.m = n - len(blacklist)
        self.map = {}
        last = n - 1        
        for b in blacklist:
            if b < self.m:
                while last in self.blacklist_set:
                    last-=1
                self.map[b] = last
                last -= 1
        

    def pick(self) -> int:
        
        idx = random.randint(0, self.m-1)
        if idx in self.map:
            return self.map[idx]
        return idx

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()