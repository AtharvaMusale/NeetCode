class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums = [1,6,2,5,8,1], k = 3
        # out= [8,6,5]
        # nums = [-1,-6,-2,-5,-8,-1]
        # [-8,-6,-5,-2,-1,-1]
        nums = [-i for i in nums]
        heapq.heapify(nums)

        
        for i in range(k):
            ans = heapq.heappop(nums)
        
        return -ans