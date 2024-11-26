class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        closest = float('inf')  # Initialize with infinity
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l<r:
                add = nums[i] + nums[l] + nums[r]
                if abs(add - target) < abs(closest- target):
                    closest  = add
                
                if add<target:
                    l+=1
                else:
                    r-=1
        return closest
