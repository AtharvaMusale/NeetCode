class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)  # Pop the largest
            second = heapq.heappop(stones)  # Pop the second largest
            
            if first != second:
                # Push the difference as negative since we're simulating a max heap
                heapq.heappush(stones, -abs(first - second))

        return abs(stones[0]) if stones else 0
            