class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def binary_search(nums):
            low = 0
            high = len(nums)-1

            while low<high:
                mid = int(low +(high-low)/2)
                if nums[mid] <= nums[mid+1]:
                    low = mid+1
                else:
                    high = mid
                
            return low
        return binary_search(nums)    
















        # def binary_search(nums):
        #     low = 0
        #     high = len(nums)-1
            

        #     while low<high:
        #         mid = int(low +(high-low)/ 2)
        #         if nums[mid] <= nums[mid+1]:
        #             low = mid+1
        #         else:
        #             high = mid
            
        #     return low
        
        # return binary_search(nums)