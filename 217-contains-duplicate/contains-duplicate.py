
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Brute FOrce- O(n^2)
        # Two loops and checking if the element is present or not
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        
        # return False

        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
            