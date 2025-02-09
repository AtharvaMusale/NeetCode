class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums = [3,2,1,5,6,4], k = 2
        # 5,4,3,2,1
        nums = [-n for n in nums]
        heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        return -nums[0]