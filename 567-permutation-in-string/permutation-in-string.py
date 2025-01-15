class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        chars1 = Counter(s1)  # Frequency map of s1
        chars2 = Counter()    # Frequency map for the sliding window in s2
        l = 0  # Left pointer for the sliding window

        for r in range(len(s2)):
            chars2[s2[r]] += 1

            # If the window size exceeds the length of s1, shrink it from the left
            if r - l + 1 > len(s1):
                chars2[s2[l]] -= 1
                if chars2[s2[l]] == 0:
                    del chars2[s2[l]]
                l += 1

            # Check if the current window matches the frequency of s1
            if chars1 == chars2:
                return True

        return False
