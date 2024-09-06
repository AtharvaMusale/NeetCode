
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()
        self.nums = nums
        for i in nums:
            if i  in hashmap:
                return True
            else:
                hashmap.add(i)
        return False