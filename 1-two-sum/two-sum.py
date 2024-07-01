class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for i in range(len(nums)):
            if target-nums[i] in hashset:
                return [i,hashset[target-nums[i]]]
            else:
                hashset[nums[i]] = i
            

        
        


















        # hashmap = {}
        # for i,j in enumerate(nums):
        #     if target-j in hashmap:
        #         return [i,hashmap[target-j]]
        #     else:
        #         hashmap[j] = i
            
            
