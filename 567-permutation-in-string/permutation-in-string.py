from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)  # Count of characters in s1
        window_count = Counter()  # Count of characters in the current window
        
        # Initialize the first window of size len(s1)
        for i in range(len(s1)):
            window_count[s2[i]] += 1
        
        if window_count == s1_count:
            return True
        
        # Slide the window over s2, one character at a time
        for i in range(len(s1), len(s2)):
            window_count[s2[i]] += 1  # Include the new character in the window
            window_count[s2[i - len(s1)]] -= 1  # Remove the character that goes out of the window
            
            # If the count goes to zero, remove it from the Counter to maintain the direct comparison
            if window_count[s2[i - len(s1)]] == 0:
                del window_count[s2[i - len(s1)]]
            
            # Check for anagram equivalence
            if window_count == s1_count:
                return True
        
        return False
