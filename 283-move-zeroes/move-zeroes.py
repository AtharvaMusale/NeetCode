class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left = 0  # Write pointer for the next non-zero position
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
