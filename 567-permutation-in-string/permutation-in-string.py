from collections import Counter
class Solution:

    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        # Frequency counts of s1 and the first window in s2
        count_s1 = Counter(s1)
        window = Counter(s2[:len(s1)])

        # Compare the initial window
        if count_s1 == window:
            return True

        # Sliding window across s2
        len_s1 = len(s1)
        for i in range(len_s1, len(s2)):
            # Add the new character to the window
            window[s2[i]] += 1
            # Remove the old character from the window
            window[s2[i - len_s1]] -= 1
            # Remove the character count from the dictionary if it drops to zero
            if window[s2[i - len_s1]] == 0:
                del window[s2[i - len_s1]]

            # Compare after each adjustment
            if count_s1 == window:
                return True

        return False
