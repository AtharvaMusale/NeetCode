class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for n in nums:
            if n in hashmap:
                hashmap[n] += 1

            else:
                hashmap[n] = 1
            
        # 1:3, 2:2, 3:1
        min_heap = []
        for val,freq in hashmap.items():
            heapq.heappush(min_heap, (freq,val))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        
        top_k = []
        while min_heap:
            top_k.append(heapq.heappop(min_heap)[1])
        return top_k