class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a":0,"e":0,"i":0,"o":0,"u":0,"A":0,"E":0,"I":0,"O":0,"U":0}
        i = j = ans = 0
        count = 0
        while j-i+1<k:
            j+=1

        for i in range(k):
            count+=int(s[i] in vowels)
        ans = count

        for i in range(k,len(s)):
            count+=int(s[i] in vowels)
            count-=int(s[i-k] in vowels)
            ans = max(ans, count)
        
        return ans




        # i = j = ans = 0
        # while j-i+1<k:
        #     j+=1

        # count = 0
        # for i in range(k):
        #     count += int(s[i] in vowels)
        # ans = count

        # for i in range(k,len(s)):a
        #     count+=int(s[i] in vowels)
        #     count-=int(s[i-k] in vowels)
        #     ans = max(ans,count)
        
        # return ans
