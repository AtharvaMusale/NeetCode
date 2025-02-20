class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l,r = 0, len(nums)-1

        while l<r:
            add = nums[l] + nums[r]

            if add>target:
                r-=1
            elif add<target:
                l+=1
            else:
                return [l+1,r+1]
        