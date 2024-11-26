class Solution:
    def maxArea(self, nums: List[int]) -> int:
        l, r  = 0, len(nums)-1
        maxArea = 0

        while l < r:
            currArea = ((r-l) * min(nums[l],nums[r]))
            maxArea = max(currArea, maxArea)

            if nums[l] > nums[r]:
                r-=1
            else:
                l+=1

        return maxArea
