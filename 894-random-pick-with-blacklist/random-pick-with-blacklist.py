import random

class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.map = {}
        blacklist_set = set(blacklist)
        self.m = n - len(blacklist)  # number of valid elements
        last = n - 1
        
        # Only remap the blacklisted elements in the range [0, self.m-1]
        for b in blacklist:
            if b < self.m:
                while last in blacklist_set:
                    last -= 1
                self.map[b] = last
                last -= 1

    def pick(self) -> int:
        idx = random.randint(0, self.m - 1)
        if idx in self.map:
            return self.map[idx]
        return idx
