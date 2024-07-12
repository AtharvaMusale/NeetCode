from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Count the frequency of each element in the list
        count = Counter(nums)
        
        # Calculate the required count threshold
        req = len(nums) // 2
        
        # Find and return the majority element
        for num in count:
            if count[num] > req:
                return num

