class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        curr = 0
        count = 0

        # Check the map
        for i in nums:
            curr+=i
            req_sum = curr - k

            if req_sum in hashmap:
                count+=hashmap[req_sum]
            
            if curr in hashmap:
                hashmap[curr] += 1
            
            else:
                hashmap[curr] = 1
            
        return count

