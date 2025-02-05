class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap = {0:-1}
        total = 0
        
        for i, val in enumerate(nums):
            total+=val
            r = total % k
            if r not in hashmap:
                hashmap[r] = i
            elif i - hashmap[r]>1:
                return True
        return False
