class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums = [1,6,2,5,8,1], k = 3
        # out= [8,6,5]
        # nums = [-1,-6,-2,-5,-8,-1]
        # [-8,-6,-5,-2,-1,-1]
        nums = [-i for i in nums]
        heapq.heapify(nums)

        for i in range(k - 1):  # Pop k-1 times to get to the k-th largest element
            heapq.heappop(nums)
        
        return -heapq.heappop(nums)  # Return the negative of the k-th pop to revert the initial negation