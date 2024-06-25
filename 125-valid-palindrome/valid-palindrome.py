class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_filtered = "".join(filter(str.isalnum,s.lower()))
        start = 0
        end = len(s_filtered)-1
        while start <= end:
            if s_filtered[start] != s_filtered[end]:
                return False
            start+=1
            end -= 1
        
        return True





        # s_filtered = ''.join(filter(str.isalnum, s.lower()))
        # start = 0
        # end = len(s_filtered) - 1
        
        # while start <= end:
        #     if s_filtered[start] != s_filtered[end]:
        #         return False
        #     start += 1
        #     end -= 1
        
        # return True
