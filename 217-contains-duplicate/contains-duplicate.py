
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         hashmap = set()
#         self.nums = nums
#         for i in nums:
#             if i  in hashmap:
#                 return True
#             else:
#                 hashmap.add(i)
#         return False
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()  # Sort the list
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:  # Check consecutive elements
                return True
        return False
