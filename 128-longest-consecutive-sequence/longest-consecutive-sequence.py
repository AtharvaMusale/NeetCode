class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        longest = 0
        for n in nums:
            # Check if (n-1) in hashSet
            if (n-1) not in hashSet:
                length = 0
                while (n+length) in hashSet:
                    length += 1
                longest = max(length, longest)
        return longest