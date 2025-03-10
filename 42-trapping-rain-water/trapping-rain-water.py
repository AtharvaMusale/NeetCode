class Solution:
    def trap(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l,r = 0, len(nums)-1
        leftMax, rightMax = nums[l], nums[r]
        res = 0
        while l<r:
            if leftMax<rightMax:
                l+=1
                leftMax = max(leftMax, nums[l])
                res += leftMax-nums[l]
            
            else:
                r-=1
                rightMax = max(rightMax, nums[r])
                res+= rightMax-nums[r]
        return res