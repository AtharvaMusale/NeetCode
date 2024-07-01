from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        hashset = set(nums)
        max_len = 0

        for num in hashset:
            # Check if it is the start of a sequence
            if num - 1 not in hashset:
                curr_num = num
                curr_len = 1

                while curr_num + 1 in hashset:
                    curr_num += 1
                    curr_len += 1

                max_len = max(max_len, curr_len)

        return max_len
