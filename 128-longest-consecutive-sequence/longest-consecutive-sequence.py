class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0
        for i in nums:
            if i-1 not in hashset:
                length = 1
                while i+length in hashset:
                    length+=1
                    
            
                longest = max(longest,length)
            
        return longest






# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         hashset = set(nums)
#         longest_streak = 0
#         for i in hashset:
#             if i-1 not in hashset:
#                 current_num = i
#                 current_streak = 1

#                 while current_num+1 in hashset:
#                     current_streak += 1
#                     current_num += 1

#                 longest_streak = max(longest_streak,current_streak)
            
#         return longest_streak