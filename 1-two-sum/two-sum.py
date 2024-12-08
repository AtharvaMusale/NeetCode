class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for ind,val in enumerate(nums):
            diff = target - val
            if diff in hashmap:
                return [ind,hashmap[diff]]
            hashmap[val] = ind
        return []
        
        