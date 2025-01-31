class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # count, current_sum, k
        # To Create a hashmap
        hashmap = {0:1}
        count = 0
        curr_sum = 0

        for ind,val in enumerate(nums):
            curr_sum += val
            if curr_sum-k in hashmap:
                count += hashmap[curr_sum-k]
            
            if curr_sum in hashmap:
                hashmap[curr_sum] += 1
            
            else:
                hashmap[curr_sum] = 1
            
        return count
