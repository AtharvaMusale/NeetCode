from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}  # A map from number to its index

        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [index, num_to_index[complement]]
            num_to_index[num] = index

        return []  # Optional: return an empty list if no solution is found
