class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def helper(x,y):
            return x**2 + y**2
        
        min_heap = []
        for x,y in points:
            dist = helper(x,y)
            heapq.heappush(min_heap, (-dist, x, y))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
            
        res = []
        for point in min_heap:
            dist,x,y = point
            res.append([x,y])

        return res