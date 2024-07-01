class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1
        
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         # Write the elements of num2 into the end of nums1.
#         for i in range(n):
#             nums1[i + m] = nums2[i]

#         # Sort nums1 list in-place.
#         nums1.sort()
# class Solution:
#     def merge(self, arr1: List[int], m: int, arr2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
        
#         p1 , p2 , p = 0, 0, 0
#         numsarr1 = arr1[:m]
#         while p<m+n:
#             if p2>=n or (p1<m and numsarr1[p1]<=arr2[p2]):
#                 arr1[p] = numsarr1[p1]
#                 p1+=1
#                 p+=1
#             else:
#                 arr1[p] = arr2[p2]
#                 p2+=1
#                 p+=1












#         # p1 =0
#         # p2=0
#         # nums1New = nums1[:m]
#         # p = 0
#         # while p< m+n:
#         #     if  p2>=n or( p1 < m and nums1New[p1] <= nums2[p2]) :
#         #         nums1[p] = nums1New[p1]
#         #         p1+=1
#         #         p+=1
#         #     else:
#         #         nums1[p] = nums2[p2]
#         #         p2+=1
#         #         p+=1

