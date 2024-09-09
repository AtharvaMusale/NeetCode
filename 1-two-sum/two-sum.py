class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for i,j in enumerate(nums):
            diff = target - j
            if diff in hashset:
                return [hashset[diff], i]
            hashset[j] = i

            