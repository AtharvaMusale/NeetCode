class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        # {1:3, 2:2, 3:1}
        min_heap = []
        for val,freq in count.items():
            heapq.heappush(min_heap, (freq,val))
            while len(min_heap) > k:
                heapq.heappop(min_heap)
            
        
        top_k = []
        while min_heap:
            freq,num = heapq.heappop(min_heap)
            top_k.append(num)
        
        return top_k