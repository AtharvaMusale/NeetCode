class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        hashset ={}

        for r in range(len(s)):
            hashset[s[r]] = 1 + hashset.get(s[r],0)

            while (r-l+1) - max(hashset.values()) > k:
                hashset[s[l]] -= 1
                l+=1
            res = max(res,(r-l+1))
        return res
        # res = 0
        # l = 0
        # hashset = {}
        # for r in range(len(s)):
        #     hashset[s[r]] = 1 + hashset.get(s[r],0)

        #     while (r-l+1) - max(hashset.values()) > k:
        #         hashset[s[l]] -= 1
        #         l+=1

        #     res = max(res, r-l+1)
        # return res
            
        # freq = defaultdict(int)
        # maxFreq = 0
        # maxLen = 0
        # i, j = 0, 0
        # while i < len(s) and j < len(s):
        #     freq[s[j]] += 1
        #     maxFreq = max(maxFreq, freq[s[j]])
        #     len_s = j-i+1
        #     isValid = len_s - maxFreq <= k
        #     if not isValid:
        #         freq[s[i]] -= 1
        #         i+=1
        #     maxLen = max(j-i+1, maxLen)
        #     j+=1
            
        # return maxLen

                


            
        