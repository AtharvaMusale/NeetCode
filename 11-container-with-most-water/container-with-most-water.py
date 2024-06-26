class Solution:
    def maxArea(self, arr: List[int]) -> int:
        left, right = 0, len(arr)-1
        res = 0
        while left<right:
            res = max(res, (right-left) * min(arr[left],arr[right]))
            if arr[left]<arr[right]:
                left += 1       
            elif arr[left] >= arr[right]:
                right -= 1

        return res

        # left , right = 0, len(arr)-1
        # result = 0

        # while left<right:
        #     result = max(result,(right-left) * min(arr[left],arr[right]))
        #     if arr[left]<arr[right]:
        #         left+=1
        #     elif arr[right]<=arr[left]:
        #         right-=1
        
        # return result