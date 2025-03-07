class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # {1:3, 2:2, 3:1}
        heap = []
        for key,val in count.items():
            heapq.heappush(heap,(val,key))
            if len(heap)>k:
                heapq.heappop(heap)

        return [val for cnt,val in heap]

