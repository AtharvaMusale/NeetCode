class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force O(n^2)
        # Hashmap
        hashmap = {}
        # [2,7,11,15] # 9
        # [2+7 = 9]
        # The array is sorted or not?
        # If Not then still O(n)
        for i,j in enumerate(nums):
            diff = target - j
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[j] = i
        return 