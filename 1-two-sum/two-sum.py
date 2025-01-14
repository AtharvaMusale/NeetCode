class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Are there Negative Numbers?
        # Can there be multiple solutions in same array?

        #Approach:
        # [2,7,11,15] 9
        hashmap = {}
        for i,num in enumerate(nums):
            diff = target - num # 7
            if diff in hashmap:
                return [i, hashmap[diff]]

            hashmap[num] = i
        return 
