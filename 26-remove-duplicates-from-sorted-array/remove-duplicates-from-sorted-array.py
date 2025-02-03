class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        ptr = 0
        n = len(nums)

        for i in range(1,n):
            curr = nums[i]
            if curr == prev:
                continue
            else:
                ptr+=1
                prev = curr
                nums[ptr] = curr       

        return ptr + 1 