class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [100,4,200,1,3,2]
        # Cant sort it
        nums = set(nums)
        longest = 0
        for num in nums:
            if num-1 in nums:
                continue
            length = 1
            while num+1 in nums:
                length+=1
                num+=1
            longest = max(longest,  length)
        return longest