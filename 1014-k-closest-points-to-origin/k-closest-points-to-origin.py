class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def cal_dist(x,y):  
            return -(x**2 + y**2)
        nums = []
        for x,y in points:
            #[1,3] #[-2,2]
            d = cal_dist(x,y)
            heapq.heappush(nums, (d,x,y))
            if len(nums)>k:
                heapq.heappop(nums)
        
        res = []
        while nums:
            d,x,y = heapq.heappop(nums)
            res.append([x,y])
        return res

