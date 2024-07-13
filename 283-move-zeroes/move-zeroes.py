class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r  = 0,0
        while l <len(nums) and r<len(nums):
            if nums[l]==0 and nums[r]!=0:
                nums[l], nums[r] = nums[r] , nums[l]
            
            r+=1
            if nums[l]!=0:
                l+=1
            


        # f,s = 0,0
        # while f<len(nums):
        #     if nums[f]!=0 and nums[s] == 0:
        #         nums[f], nums[s] = nums[s], nums[f]
            
        #     if nums[s]!=0:
        #         s+=1
        #     f+=1


        