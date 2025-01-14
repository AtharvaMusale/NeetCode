class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # What for empty array?
        # Can I use heap?

        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        heap = []
        for n in count.keys():
            heapq.heappush(heap, (count[n],n))
            if len(heap)>k:
                heapq.heappop(heap)
            
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

