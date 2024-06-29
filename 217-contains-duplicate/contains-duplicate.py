class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(list(set(nums)))!=len(nums)


# # Time complexity: O(n)
# # Space complexity: O(n)
# class Solution(object):
#     def containsDuplicate(self, nums):
#         hset = set()
#         for idx in nums:
#             if idx in hset:
#                 return True
#             else:
#                 hset.add(idx)