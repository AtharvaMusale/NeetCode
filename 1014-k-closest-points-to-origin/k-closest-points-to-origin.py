class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def cal_dist(x,y):
            return x**2 + y**2
        

        heap = []

        for u,v in points:
            dist = cal_dist(u,v)
            heap.append([dist,(u,v)])
        
        heapq.heapify(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
