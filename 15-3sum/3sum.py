class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)-2):
            if i >0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i+1, len(nums)-1
            while l<r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l+=1
                elif total > 0:
                    r-=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l+= 1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return res





        # res = []
        # nums.sort()

        # for i, a in enumerate(nums):
        #     # Skip positive integers
        #     if a > 0:
        #         break

        #     if i > 0 and a == nums[i - 1]:
        #         continue

        #     l, r = i + 1, len(nums) - 1
        #     while l < r:
        #         threeSum = a + nums[l] + nums[r]
        #         if threeSum > 0:
        #             r -= 1
        #         elif threeSum < 0:
        #             l += 1
        #         else:
        #             res.append([a, nums[l], nums[r]])
        #             l += 1
        #             r -= 1
        #             while nums[l] == nums[l - 1] and l < r:
        #                 l += 1
                        
        # return res
