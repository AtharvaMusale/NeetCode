class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        # [-3,-2,-1,-5,-6,-4]
        heapq.heapify(nums)
        # [-6,-5,-4,-3,-2,-1]
        for i in range(k-1):
            heapq.heappop(nums)
        
        return -nums[0]