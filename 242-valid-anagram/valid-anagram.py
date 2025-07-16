class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charS, charT = defaultdict(int), defaultdict(int)
        for i, val in enumerate(s):
            charS[val] = 1 + charS.get(val, 0)

        for i, val in enumerate(t):
            charT[val] = 1 + charT.get(val, 0)
        return charS==charT