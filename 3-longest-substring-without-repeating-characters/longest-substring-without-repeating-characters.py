class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        start = 0
        max_len = 0

        for end, val in enumerate(s):
            if val in hashmap and hashmap[val] >= start:
                start = hashmap[val] + 1

            hashmap[val] = end
            max_len = max(max_len, end-start+1)
        
        return max_len

