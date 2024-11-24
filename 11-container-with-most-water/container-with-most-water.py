class Solution:
    def maxArea(self, nums: List[int]) -> int:
        l, r = 0, len(nums) -1
        res = 0
        while l<r:
            
            curr_area =  (r-l) * min(nums[r],nums[l])
            res = max(curr_area,res)

            if nums[l]<nums[r]:
                l+=1
            else:
                r-=1
        
        return res