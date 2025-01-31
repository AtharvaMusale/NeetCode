class Solution:
    def merge(self, nums: List[List[int]]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort(key = lambda x:x[0])

        res = []
        for num in nums:
            start, end = num
        
            if not res or res[-1][1] < start:
                res.append(num)
            
            else:
                res[-1][1] = max(res[-1][1], num[1])
        
        return res