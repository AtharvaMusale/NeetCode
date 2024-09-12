class Solution:
    def maxArea(self, nums: List[int]) -> int:
        l, r  = 0, len(nums)-1

        total_area = 0

        while l<r:
            area = min(nums[l],nums[r]) * (r-l)
            total_area = max(total_area,area)
            if nums[l]<nums[r]:
                l+=1
            else:
                r-=1
        return total_area
