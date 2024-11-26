# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
        
#         nums.sort()
#         closest = float('inf')  # Initialize with infinity
#         for i in range(len(nums)-2):
#             l, r = i+1, len(nums)-1
#             while l<r:
#                 add = nums[i] + nums[l] + nums[r]
#                 if abs(add - target) < abs(closest- target):
#                     closest  = add
                
#                 if add<target:
#                     l+=1
#                 else:
#                     r-=1
#         return closest


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float("inf")
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                complement = target - nums[i] - nums[j]
                hi = bisect_right(nums, complement, j + 1)
                lo = hi - 1
                if hi < len(nums) and abs(complement - nums[hi]) < abs(diff):
                    diff = complement - nums[hi]
                if lo > j and abs(complement - nums[lo]) < abs(diff):
                    diff = complement - nums[lo]
            if diff == 0:
                break
        return target - diff