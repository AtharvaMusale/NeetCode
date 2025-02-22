class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x,y):
            return x**2 + y**2
        
        heap = []
        for x,y in points:
            dist = distance(x,y)
            heapq.heappush(heap,(-dist,x,y))
            while len(heap)>k:
                heapq.heappop(heap)

        res = []
        for p in heap:
            dist,x,y = p
            res.append([x,y])
        return res
