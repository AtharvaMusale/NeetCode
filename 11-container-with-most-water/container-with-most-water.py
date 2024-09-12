class Solution:
    def maxArea(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        max_area = 0

        while l < r:
            # Calculate the area for the current left and right pointers
            height = min(nums[l], nums[r])
            width = r - l
            max_area = max(max_area, height * width)

            # Move the pointer pointing to the shorter line inward
            if nums[l] < nums[r]:
                l += 1
            else:
                r -= 1
                
        return max_area
