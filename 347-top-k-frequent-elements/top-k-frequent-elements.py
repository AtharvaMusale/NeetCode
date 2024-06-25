from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        count = Counter(nums)

        return heapq.nlargest(k, count.keys(), key = count.get)


















# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         cnt = collections.Counter(nums)
#         unique = list(cnt.items())  # (number, frequency) pairs list
#         print(unique)
#         n = len(unique)
#         self.quickselect(unique, 0, len(unique) - 1,n -k)

#         return [pair[0] for pair in unique[n-k:]]


#     def quickselect(self, arr, low, high, k):
#         if low == high:
#             return arr[low]

#         i = self.partition(arr, low, high)
#         if k == i:
#             return arr[k]
#         elif k < i:
#             return self.quickselect(arr, low, i - 1, k)
#         else:
#             return self.quickselect(arr, i + 1, high, k)


#     def partition(self, arr, low, high):
#         pivot = arr[high][1]
#         i = low
#         for j in range(low, high):
#             if arr[j][1] <= pivot:
                
#                 arr[i], arr[j] = arr[j], arr[i]
#                 i+=1
      
#         arr[i], arr[high] = arr[high], arr[i]

#         return i