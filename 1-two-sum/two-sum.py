class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in hashmap:
                return [i,hashmap[diff]]
            hashmap[val] = i
        return 