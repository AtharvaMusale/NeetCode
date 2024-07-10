class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1 = p2 = 0
        merge = []
        while p1 < len(nums1) and p2< len(nums2):
            if nums1[p1] <= nums2[p2]:
                merge.append(nums1[p1])
                p1+=1
            else:
                merge.append(nums2[p2])
                p2+=1
            
        while p1<len(nums1):
            merge.append(nums1[p1])
            p1+=1
        
        while p2< len(nums2):
            merge.append(nums2[p2])
            p2+=1
        
        n = len(merge)
        if n%2!=0:
            return float(merge[int(n/2)])

        return float((merge[(n-1)//2] + merge[n//2])/2.0)

        # p1 = 0
        # p2 = 0
        # merge = []
        # while p1<len(nums1) and p2<len(nums2):
        #     if nums1[p1]<=nums2[p2]:
        #         merge.append(nums1[p1])
        #         p1+=1
        #     else:
        #         merge.append(nums2[p2])
        #         p2+=1
            
        # while p1<len(nums1):
        #     merge.append(nums1[p1])
        #     p1+=1

        # while p2<len(nums2):    
        #     merge.append(nums2[p2])
        #     p2+=1

        # n = len(merge)
        # if n % 2 != 0:
        #     return float(merge[int(n/2)])
    
        # return float((merge[(n - 1) // 2] + merge[n // 2]) / 2.0)