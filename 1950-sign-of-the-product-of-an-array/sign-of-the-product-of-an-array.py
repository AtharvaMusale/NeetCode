class Solution:
    def arraySign(self, nums: List[int]) -> int:
        mul = 1
        for i in range(len(nums)):
            mul *=  nums[i]
        
        if mul<0:
            return -1
        elif mul == 0:
            return 0
        elif mul > 0:
            return 1