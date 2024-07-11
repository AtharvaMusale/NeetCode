class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left, right = 0,0
        while left<len(s) and right < len(t):
            if s[left] == t[right]:
                left+=1
            right += 1
        return left==len(s)
        # LEFT_BOUND, RIGHT_BOUND = len(s), len(t)
        # left,right = 0,0
        # while left<len(s) and right<len(t):
        #     if s[left] == t[right]:
        #         left+=1
        #     right+=1
        # return left==LEFT_BOUND
                









    # def isSubsequence(self, s: str, t: str) -> bool:
    #     LEFT_BOUND, RIGHT_BOUND = len(s), len(t)

    #     def is_subsequence(left_index,right_index):
    #         if left_index == LEFT_BOUND:
    #             return True
            
    #         if right_index == RIGHT_BOUND:
    #             return False
            
    #         if s[left_index] == t[right_index]:
    #             left_index+=1
            
    #         right_index+=1
    #         return is_subsequence(left_index,right_index)
    
    #     return is_subsequence(0,0)