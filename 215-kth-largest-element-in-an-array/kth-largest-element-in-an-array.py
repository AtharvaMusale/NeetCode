class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        # [-3,-2,-1,-5,-6,-4]
        heapq.heapify(nums)
        for _ in range(k-1):
            heapq.heappop(nums)
        return -nums[0]
        
        