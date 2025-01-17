class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [4,5,6,7,0,1,2] Rotated 4 times
        # [0,1,2,4,5,6,7] Rotated 0 or 7 times
        # Unique Elements, Return Min Element
        # If mid element > rth element: Right array is sorted and smaller so we go right
        #  Else Left
        #  Can there be duplicates?

        l , r = 0, len(nums)-1
        while l<r:
            m = (l+r)//2
            if nums[m]>=nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]

