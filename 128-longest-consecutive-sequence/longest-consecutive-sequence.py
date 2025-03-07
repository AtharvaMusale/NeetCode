class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for n in nums:
            if n-1 in nums:
                continue
            length = 1
            while n+1 in nums:
                length+=1
                n+=1
            longest = max(longest,length)
                
        return longest