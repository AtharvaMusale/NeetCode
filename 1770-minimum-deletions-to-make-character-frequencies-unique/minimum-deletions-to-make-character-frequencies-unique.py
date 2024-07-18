class Solution:
    def minDeletions(self, s: str) -> int:
        hashmap = collections.Counter(s)
        hashset = set()
        res =0
        for c, freq in hashmap.items():
            while freq>0 and freq in hashset:
                freq-=1
                res+=1
            hashset.add(freq)
        return res