import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # x==y borth destroy
        #  x<=y y-x
        stones = [-i for i in stones]
        heapq.heapify(stones)

        # 1,2,4,3,7
        # -7,-4,-3,-2,-1
        #  -7, -4
        while len(stones)>1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)   
            if a == b:
                continue
            if a<b:
                heapq.heappush(stones,-abs(b-a))
            
        return -stones[0] if stones else 0