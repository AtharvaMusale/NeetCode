class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        curr = 0
        count = 0
        for i, val in enumerate(nums):
            curr += val
            if (curr - k) in hashmap:
                count += hashmap[curr-k]

            if curr in hashmap:
                hashmap[curr] += 1
            
            else:
                hashmap[curr] = 1
        return count