class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        l=nums1+nums2
        l.sort()
        if (n+m)%2==1:
            return l[((n+m)//2)]
        else:
            median=(l[(n+m)//2]+l[((n+m)//2)-1])/2

            return median

        