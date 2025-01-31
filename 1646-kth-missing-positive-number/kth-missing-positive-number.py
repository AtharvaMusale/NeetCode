# class Solution:
#     def findKthPositive(self, arr: List[int], k: int) -> int:
#         miss = 0
#         arr_max = max(arr)

#         for i in range(1,arr_max):
#             if i not in arr:
#                 miss+=1
        
#         if k-miss>0:
#             return arr_max + k - miss
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr)

        while left < right:
            mid = (left + right) // 2
            # Check how many numbers are missing until arr[mid]
            if arr[mid] - (mid + 1) < k:
                left = mid + 1
            else:
                right = mid

        # If we exhaust the list, then the answer is outside the max value in array
        # (left) + k - the number of missing numbers before the last element in array
        return left + k
