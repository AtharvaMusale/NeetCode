class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Can there be negative numbers?
        # Can there be duplicates?
        # 

        # Approach:
        # i,j,k 3 ptr, Sort the input -> Fix One Pointer -> Use other two for Condition check

        res = []
        nums.sort()

        # [-4,-4,-1,0,1,2]
        for i in range(len(nums)-2):
            #-4
            if nums[i]>0:
                break
            
            if i>0 and nums[i] == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1

            while l<r:
                add = nums[i] + nums[l] + nums[r]
                if add>0:
                    r-=1
                elif add<0:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res 

