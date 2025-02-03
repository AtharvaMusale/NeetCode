class Solution:
    def isPalindrome(self, s: str) -> bool:
        #  Convert to lowercase
        # l = r  while l<=r and each char is alphanumeric then compare and adjust   
        l = 0
        r = len(s)-1
        s = s.lower()
        while l< r:
            while l<=r and not s[l].isalnum():
                l+=1
            while l<=r and not s[r].isalnum():
                r-=1
            
            if l<r and s[l]!=s[r]:
                return False

            l+=1
            r-=1

        return True