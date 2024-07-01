class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        bad_index = l_index = r_index = -1
        res = 0

        for i,j in enumerate(nums):
            if not minK <= j <=maxK:
                bad_index = i
            
            if j == minK:
                l_index = i
            
            if j == maxK:
                r_index = i
            
            res += max(0,(min(l_index,r_index)-bad_index))
        
        return res