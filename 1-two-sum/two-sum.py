class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i,j in enumerate(nums):
            
            if (target - j) in hashmap:
                return [i,hashmap[target - j]]
            
            hashmap[j] = i
        