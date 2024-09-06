class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for ind, val in enumerate(nums):
            if val in hashmap:
                return [ind , hashmap[val]]
            hashmap[target-val] = ind
        return []
        
            