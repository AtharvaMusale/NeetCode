# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         # hashset = set(nums)
#         # longest = 0
#         # for n in nums:
#         #     if n-1 not in hashset:
#         #         length = 1
#         #         while (n+length) in hashset:
#         #             length+=1
                
#         #         longest = max(longest,length)

#         # return longest

#         hashSet = set(nums)
#         longest = 0
#         for n in nums:
#             # Check if (n-1) in hashSet
#             if (n-1) not in hashSet:
#                 length = 1
#                 while (n+length) in hashSet:
#                     length += 1
#                 longest = max(length, longest)
#         return longest

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        prev_num = nums[0]
        max_size = 1
        current_size = 1
        for i in nums:
            if (prev_num+1) == i:
                current_size +=1 
                if current_size > max_size:
                    max_size = current_size
            elif prev_num == i:
                pass
            else:
                current_size = 1
            prev_num = i
        return max_size
        