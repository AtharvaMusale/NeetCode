class Solution:
    def lastStoneWeight(self, nums: List[int]) -> int:
        nums = [-n for n in nums]
        # [-2,-7,-4,-1,-8,-1]
        heapq.heapify(nums)
        # [-8,-7,-4,-2,-1,-1]

        while len(nums)>1:
            a = heapq.heappop(nums)
            b = heapq.heappop(nums)
            # -8,-7
            if b>a:
                heapq.heappush(nums,(a-b))
        
        nums.append(0)
        return abs(nums[0])
            