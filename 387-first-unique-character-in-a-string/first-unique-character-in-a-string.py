class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        for ind, ch in enumerate(s):
            if count[ch] == 1:
                return ind
        return -1