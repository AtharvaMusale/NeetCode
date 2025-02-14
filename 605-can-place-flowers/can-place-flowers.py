# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         bed = [0] + flowerbed + [0]
#         for i in range(1,len(bed)-1):
#             if bed[i] == bed[i-1] == bed[i+1] == 0:
#                 n-=1
#                 bed[i] = 1
            
#         return n<=0

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    
        for i in range(len(flowerbed)):
            left = i == 0 or flowerbed[i-1] == 0
            right = i == len(flowerbed) - 1 or flowerbed[i+1] == 0

            if left and right and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
        
        return n <= 0