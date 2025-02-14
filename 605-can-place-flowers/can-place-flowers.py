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
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False