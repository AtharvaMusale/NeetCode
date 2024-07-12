class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currSum = 0
        prefixSum = {0:1}
        for i in range(len(nums)):
            currSum += nums[i]
            diff =  currSum - k

            res += prefixSum.get(diff,0)
            prefixSum[currSum] = 1+ prefixSum.get(currSum,0)
        return res



        # hashmap = defaultdict(int) #cumulative sum up to all the indices possible
        # along with the number of times the same sum occurs. sum[i] -sum[j] = k, then sum[i]-k = sum[j]

        # psum = 0
        # ans = 0
        # hashmap[0] = 1

        # for n in nums:
        #     psum += n
        #     if psum-k in hashmap:
        #         ans += hashmap[psum-k]
            
        #     hashmap[psum] = hashmap[psum]+1
        
        # return ans