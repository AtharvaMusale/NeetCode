class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        ans = 0
        index = len(nums1)//2
        if len(nums1)%2 == 0:
            ans = (nums1[index] + nums1[index-1])/2
        else:
            ans = nums1[index]
        return ans

        