from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = defaultdict(int)
        window_size = 0
        max_len = 0
        max_freq = 0
        l = 0

        for r in range(len(s)):
            char_count[s[r]]+=1
            max_freq = max(max_freq, char_count[s[r]])
            window_size = r-l+1
            if (window_size-max_freq)>k:
                char_count[s[l]]-=1
                l+=1
            
            max_len = max(max_len,r-l+1)
        
        return max_len