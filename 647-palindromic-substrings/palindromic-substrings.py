class Solution:
    def countSubstrings(self, s: str) -> int:
        def expandCentre(l,r):
            count = 0
            while l>=0 and r<len(s) and s[l] == s[r]:
                count+=1
                l-=1
                r+=1
            return count

        

        total = 0
        for i in range(len(s)):
            total += expandCentre(i,i)
            total+= expandCentre(i,i+1)
        return total