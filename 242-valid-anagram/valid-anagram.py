class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charS, charT = {}, {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            charS[s[i]] = 1 + charS.get(s[i],0)
            charT[t[i]] = 1 + charT.get(t[i],0)
        return charS == charT
        