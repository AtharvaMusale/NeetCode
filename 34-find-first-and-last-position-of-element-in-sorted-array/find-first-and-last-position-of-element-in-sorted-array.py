class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binary(leftB):
            l ,r = 0, len(nums)-1
            i = -1
            while l <= r:
                m = l + ((r-l)//2)
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m-1
                else:
                    i = m
                    if leftB:
                        r = m - 1
                    else:
                        l = m + 1
            return i
        left = binary(True)
        right = binary(False)
        return [left,right]