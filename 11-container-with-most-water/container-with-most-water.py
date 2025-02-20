class Solution:
    def maxArea(self, nums: List[int]) -> int:
        max_area = 0
        area = 0
        l,r = 0,len(nums)-1

        while l<r:
            area = ((r-l) * min(nums[l],nums[r]))
            if area>max_area:
                max_area = area
            if nums[l]<=nums[r]:
                l+=1
            else:
                r-=1
           
        return max_area