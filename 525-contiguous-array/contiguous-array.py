from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_map = {0: -1}
        maxlen = 0
        count = 0
        
        for i in range(len(nums)):
            count += 1 if nums[i] == 1 else -1
            if count in count_map:
                maxlen = max(maxlen, i - count_map[count])
            else:
                count_map[count] = i
        
        return maxlen

# class Solution:
#     def findMaxLength(self, nums: List[int]) -> int:
#         hashmap = {}
#         for i in range(len(nums)):
            
        # mp = dict()
        # currSum = 0
        # mp[0] = -1
        # maxLen = 0
        # for i, num in enumerate(nums):
            
        #     if num == 0:
        #         currSum += -1
        #     else:
        #         currSum += 1
        #     if currSum in mp:
        #         maxLen = max(maxLen, i-mp[currSum])
        #     else:
        #         mp[currSum] = i
        #     print(mp)

        # return maxLen
            
        

# 0  1  0  0  1  0
# -1 0 -1 -2 -1