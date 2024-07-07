class Solution:
    def maxArea(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)-1
        area = 0
        while l<r:
            area = max(area, (r-l) * (min(arr[l], arr[r])))
            if arr[l] < arr[r]:
                l+=1
            else:# arr[l]>=arr[r]:
                r-=1
        
        return area



        # left, right = 0, len(arr)-1
        # res = 0
        
        # while left<right:
        #     res = max(res, (right-left) * min(arr[left],arr[right]))
        #     if arr[left]<arr[right]:
        #         left += 1       
        #     elif arr[left] >= arr[right]:
        #         right -= 1

        # return res

        # left , right = 0, len(arr)-1
        # result = 0

        # while left<right:
        #     result = max(result,(right-left) * min(arr[left],arr[right]))
        #     if arr[left]<arr[right]:
        #         left+=1
        #     elif arr[right]<=arr[left]:
        #         right-=1
        
        # return result