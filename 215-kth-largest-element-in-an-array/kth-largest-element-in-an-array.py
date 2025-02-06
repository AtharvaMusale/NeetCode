import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k]  # Take first `k` elements
        heapq.heapify(min_heap)  # Convert to a min-heap

        for num in nums[k:]:  # Process remaining elements
            if num > min_heap[0]:  # Compare with the smallest in heap
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)

        return min_heap[0]  # The root of the heap is the k-th largest element
