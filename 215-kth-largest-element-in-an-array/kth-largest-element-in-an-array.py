# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         min_heap = []
#         for i in nums:
#             heapq.heappush(min_heap, i)
#             if len(min_heap)>k:
#                 heapq.heappop(min_heap)
#         return min_heap[0]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Use a min-heap of size k to find the k-th largest element
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]
