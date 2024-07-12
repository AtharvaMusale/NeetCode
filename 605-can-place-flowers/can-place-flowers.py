class Solution:
    def canPlaceFlowers(self, arr: List[int], n: int) -> bool:
        arr = [0] + arr + [0]
        for i in range(1,len(arr)-1):
            if arr[i-1] == 0 and arr[i] == 0 and arr[i+1] == 0:
                arr[i] = 1
                n-=1
        return n <=0

            
        # count=0
        # for i in range(len(arr)):
        #     if arr[i]==0:
        #         empty_left_plot = (i==0) or (arr[i-1]==0)
        #         empty_right_plot = (i==len(arr)-1) or (arr[i+1]==0)
        #         if empty_left_plot and empty_right_plot:
        #             arr[i] = 1
        #             count+=1
        # return count>=n
