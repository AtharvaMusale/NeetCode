class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        global_sum = float("-inf")
        l= 0
        curr_sum = 0

        for r in range(len(nums)):
            curr_sum += nums[r]
            if r-l+1 == k:
                global_sum = max(global_sum, curr_sum)
                curr_sum -= nums[l]
                l+=1
            
        return global_sum / k
            
