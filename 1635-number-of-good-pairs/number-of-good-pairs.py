class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        hashmap = defaultdict(int)
        for i in nums:
            ans+=hashmap[i]
            hashmap[i]+=1
        return ans
            
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             count+=1
        
        # return count