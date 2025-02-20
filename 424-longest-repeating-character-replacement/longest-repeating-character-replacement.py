class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxf= 0
        res = 0
        hashmap = {}
        for r in range(len(s)):
            hashmap[s[r]] = 1 + hashmap.get(s[r],0)
            maxf = max(maxf,hashmap[s[r]])
            while (r-l+1) - maxf >k:
                hashmap[s[l]]-=1
                l+=1
        
            res = max(res,r-l+1)
        return res