class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1+ count.get(n,0)

        min_heap = []
        for val,count in count.items():
            heapq.heappush(min_heap, (count,val))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        
        # Extract the elements from the heap
        return [val for cnt, val in min_heap]