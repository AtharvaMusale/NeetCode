class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x,y):
            return x**2 + y**2
    
        min_heap = []
        for x,y in points:
            dist = distance(x,y)
            heapq.heappush(min_heap, (-dist,x,y))
            while len(min_heap) > k:
                heapq.heappop(min_heap)
            
        res = []
        for point in min_heap:
            dist, x, y = point
            res.append([x,y])
        return res