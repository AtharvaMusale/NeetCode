class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT , window = {}, {}
        have = 0

        if t == "":
            return ""

        for i in t:
            countT[i] = 1 + countT.get(i,0)

        need = len(countT)
        res, resLen = [-1,-1], float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)
        
            if c in countT and window[c] == countT[c]:
                have+=1
            
            while have == need:
                # Update the result
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = (r-l+1)
                
                # Pop from the left of the window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have-=1

                l+=1
        l,r = res
        return s[l:r+1] if resLen!= float("inf") else ""
































        # if t == "": return ""
        # countT = Counter(t)
        # window = defaultdict(int)
        # have, need = 0, len(countT)
        # ans, minLen = "", float('inf')
        # i, j = 0, 0
        # while j < len(s):
        #     currChar = s[j]
        #     window[s[j]]+=1
        #     if window[s[j]] == countT[s[j]]:
        #         have+=1
        #     while have == need:
        #         if minLen > j-i+1:
        #             minLen = j-i+1
        #             ans = s[i:j+1]
        #         window[s[i]] -= 1
        #         if s[i] in countT and window[s[i]] < countT[s[i]]:
        #             have-=1
        #         i+=1
        #     j+=1
        # return ans


