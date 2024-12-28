from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)  # Count the frequency of each element
        
        # Use a min-heap of size k
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)  # Remove the element with the smallest frequency
        
        # Extract the elements from the heap
        return [num for freq, num in heap]
