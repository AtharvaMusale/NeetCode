class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        # [2,7,11,15] target = 9
        for i, val in enumerate(nums):
            diff = target - val
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[val] = i
        return 