class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        # hasmap[Value] = index
        for i,j in enumerate(nums):
            diff = target - j
            if j in hashmap:
                return [hashmap[j], i]
            else:
                hashmap[diff] = i 

        