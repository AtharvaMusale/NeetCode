# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # heap = []
        # heapify(heap)
        # for i in arr:
        #     heappush(heap,(abs(x-i),i))
        
        # res = []
        # while k>0:
        #     res.append(heappop(heap)[1])
        #     k-=1
        
        # return sorted(res)

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Sort using custom comparator
        sorted_arr = sorted(arr, key = lambda num: abs(x - num))

        # Only take k elements
        result = []
        for i in range(k):
            result.append(sorted_arr[i])
        
        # Sort again to have output in ascending order
        return sorted(result)











        # heap = []
        # heapify(heap)
        # for i in arr:
        #     heappush(heap,(abs(x-i),i))
                
        # res=[]  
        # while k > 0:
        #     res.append(heappop(heap)[1])
        #     k -= 1
        
        # return sorted(res)
