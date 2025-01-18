class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # [2,7,4,1,8,1] 
        
        # x = 7 , y= 8
        stones = [-s for s in stones]
        heapq.heapify(stones) # [-8,-7,-4,-2,-1,-1]
        while len(stones)>1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
        
            if y > x:
                heapq.heappush(stones, x-y)

        stones.append(0)
        return -stones[0]
