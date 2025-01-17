class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [-1, 0, 3, 5, 9, 12]
        l = 0
        r = len(nums)-1

        while l<=r:
            m = l + ((r-l)//2)

            if nums[m] < target:
                l += 1
            elif nums[m]>target:
                r -= 1
            else:
                return m
            
        return -1
