class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Build the window of size k, count the number of vowels it contains.
        count = 0
        for i in range(k):
            count += int(s[i] in vowels)
        answer = count
        
        # Slide the window to the right, focus on the added character and the
        # removed character and update "count". Record the largest "count".
        for i in range(k, len(s)):
            count += int(s[i] in vowels)
            count -= int(s[i - k] in vowels)
            answer = max(answer, count)
        
        return answer




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
