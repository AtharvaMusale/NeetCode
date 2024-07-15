class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-s for s in nums]
        heapq.heapify(nums)
        while k>0:
            q = heapq.heappop(nums)
            k-=1
        return -q
       
       
       
       
       
       
       
       
       
       
        # minHeap = []
        # for i in nums:
        #     heapq.heappush(minHeap,i)
        #     if len(minHeap)>k:
        #         heapq.heappop(minHeap)
        
        # return minHeap[0]


        