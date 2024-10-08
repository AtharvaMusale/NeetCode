class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        # hasmap[Value] = index
        for i,j in enumerate(nums):
            diff = target - j
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[j] = i
        