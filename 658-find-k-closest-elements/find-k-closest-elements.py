class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        heapify(heap)
        for i in arr:
            heappush(heap,(abs(x-i),i))
        
        res = []
        while k>0:
            res.append(heappop(heap)[1])
            k-=1
        
        return sorted(res)













        # heap = []
        # heapify(heap)
        # for i in arr:
        #     heappush(heap,(abs(x-i),i))
                
        # res=[]  
        # while k > 0:
        #     res.append(heappop(heap)[1])
        #     k -= 1
        
        # return sorted(res)
