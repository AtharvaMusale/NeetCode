class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l = total = 0
        res = float('inf')

        for i in range(len(nums)):
            total += nums[i]
            while total >= s:
                res = min(res,i-l+1)
                total-=nums[l]
                l+=1
        
        return res if res!=float("inf") else 0
            






























        # res = float("inf")
        # left, total = 0, 0
        
        # for i in range(len(nums)):
        #     total += nums[i]
        #     while total >= s:
        #         res = min(res, i - left + 1)
        #         total -= nums[left]
        #         left += 1
        
        # return res if res != float("inf") else 0