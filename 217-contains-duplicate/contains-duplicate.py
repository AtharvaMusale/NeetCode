# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         hashset = set()
#         for n in nums:
#             if n in hashset:
#                 return True
#             hashset.add(n)
#         return False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True