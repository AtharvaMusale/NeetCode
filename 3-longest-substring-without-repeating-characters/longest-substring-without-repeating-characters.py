class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # [abcabcbb]
        # l = a r = a # curr_len = r-l+1 # MaxLen = max(max_len, curr_len)
        l = 0
        hashset = set()
        res = 0

        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l+=1
            hashset.add(s[r])

            res = max(res,r-l+1)
        
        return res