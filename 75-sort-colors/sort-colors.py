class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mid = 0
        i=0
        j = len(nums)-1
        while j >= mid:
            
            if nums[mid] == 0:
                nums[mid], nums[i] = nums[i], nums[mid]
                i+=1
                mid+=1
            elif nums[mid] == 2:
                nums[mid], nums[j] = nums[j], nums[mid]
                j-=1
            else:
                mid+=1
        return nums

# class Solution:
#     def sortColors(self, l: List[int]) -> None:
#         n=len(l)
#         for i in range(n-1):
#             for j in range(i+1,n):
#                 if(l[i]>l[j]):
#                     l[i],l[j]=l[j],l[i]