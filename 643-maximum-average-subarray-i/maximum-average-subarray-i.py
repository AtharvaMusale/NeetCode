from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        # Initialize curr_sum with first k elements
        curr_sum = sum(nums[:k])
        global_sum = curr_sum  # First k elements sum is our initial max sum

        for r in range(k, len(nums)):  # Start from k since first window is precomputed
            curr_sum += nums[r] - nums[r - k]  # Sliding window update
            global_sum = max(global_sum, curr_sum)  # Track maximum sum

        return global_sum / k  # Compute average
