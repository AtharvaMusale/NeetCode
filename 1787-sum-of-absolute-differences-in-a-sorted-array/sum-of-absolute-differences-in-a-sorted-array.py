class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [nums[0]]

        for i in range(1,n):
            prefix.append(nums[i] + prefix[-1])
        
        ans = []

        for i in range(len(nums)):
            left_sum = prefix[i] - nums[i]
            right_sum = prefix[-1] - prefix[i]

            left_count = i
            right_count = n-i-1

            left_total = left_count * nums[i] - left_sum
            right_total = right_sum - right_count * nums[i]

            ans.append(left_total + right_total)
        
        return ans