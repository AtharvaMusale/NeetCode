class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
#         # hashset = set(nums)
#         # longest = 0
#         # for n in nums:
#         #     if n-1 not in hashset:
#         #         length = 1
#         #         while (n+length) in hashset:
#         #             length+=1
                
#         #         longest = max(longest,length)

#         # return longest

        hashset = set(nums)
        longest = 0
        for i in nums:
            if i-1 not in hashset:
                length = 1
                while i+length in hashset:
                    length+=1
                longest = max(longest, length)
        return longest