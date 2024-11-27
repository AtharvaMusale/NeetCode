# from collections import defaultdict

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if t == "":
#             return ""
        
#         countT, countS = {}, {}
#         for c in t:
#             countT[c] = 1 + countT.get(c , 0)

#         have, need = 0 ,len(countT)
#         l = 0
#         res, resLen = [-1,-1], float('inf')

#         for r in range(len(s)):
#             c = s[r]
#             countS[c] = 1+ countS.get(c,0)

#             if c in countT and countS[c] == countT[c]:
#                 have +=1
            
#             while have == need:
#                 if (r-l+1) < resLen:
#                     resLen = (r-l+1)
#                     res = [l,r]
#                 # Pop from left
#                 countS[s[l]] -= 1
#                 if s[l] in countT and countS[s[l]] < countT[s[l]]:
#                     have -= 1
#                 if countS[s[l]] == 0:
#                     del countS[s[l]]
#                 l+=1
#         l,r = res
#         return s[l:r+1] if resLen != float("inf") else ""


from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT = defaultdict(int)
        for c in t:
            countT[c] += 1

        countS = defaultdict(int)
        have, need = 0, len(countT)
        l = 0
        res, resLen = [-1, -1], float('inf')

        for r in range(len(s)):
            c = s[r]
            if c in countT:
                countS[c] += 1
                if countS[c] == countT[c]:
                    have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = (r - l + 1)
                    res = [l, r]
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                if countS[s[l]] == 0:
                    del countS[s[l]]  # Delete zero count entries to save space
                l += 1

        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""
