class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        bed = [0] + flowerbed + [0]
        for i in range(1,len(bed)-1):
            if bed[i] == bed[i-1] == bed[i+1] == 0:
                n-=1
                bed[i] = 1
            
        return n<=0