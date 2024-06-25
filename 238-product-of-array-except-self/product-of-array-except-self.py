class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        
        L, R, result = [1]*length,[1]*length, [1]*length
        for i in range(1,len(nums)):
            L[i] = L[i-1] * nums[i-1]
        
        R[length-1] = 1
        for i in reversed(range(length-1)):
            R[i] = nums[i+1] * R[i+1]
        
        for i in range(length):
            result[i] = L[i]*R[i]
        
        return result

