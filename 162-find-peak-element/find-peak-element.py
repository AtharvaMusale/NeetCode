class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1

        while l<r:
            m = (l+r)//2
            if nums[m]>=nums[m-1] and nums[m]>=nums[m+1]:
                return m
            elif nums[m+1]>nums[m]:
                l = m + 1
            elif nums[m-1] > nums[m]:
                r = m - 1

        return l
