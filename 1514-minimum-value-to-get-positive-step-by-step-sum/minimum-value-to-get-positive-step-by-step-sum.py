class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_val = 0
        total = 0
        for i in nums:
            total+=i
            min_val = min(min_val,total)
        
        return 1-min_val