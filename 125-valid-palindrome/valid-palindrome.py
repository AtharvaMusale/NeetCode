class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l <= r:
            # Skip non-alphanumeric characters for the left pointer
            if not s[l].isalnum():
                l += 1
            # Skip non-alphanumeric characters for the right pointer
            elif not s[r].isalnum():
                r -= 1
            # Compare the characters (ignore case)
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
                
        return True
