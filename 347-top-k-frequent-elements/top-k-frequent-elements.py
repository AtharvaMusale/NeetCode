from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        count = Counter(nums)
        arr = []
        for num,freq in count.iterms():
            heapq.heappush(arr,(-freq, num))
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(arr)[1])
        
        return result
        
        

        

        










#         # count = Counter(nums)
#         # heap = []
#         # for num, freq in count.items():
#         #     heapq.heappush(heap, (-freq, num))
        
#         # result = []
#         # for i in range(k):
#         #     result.append(heapq.heappop(heap)[1])
        
#         # return result



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # find the frequency of each number
        num_frequency_map = {}
        for num in nums:
            num_frequency_map[num] = num_frequency_map.get(num, 0) + 1
        top_k_elements = []

        # go through all numbers of the num_frequency_map
        # and push them in the top_k_elements, which will have
        # top k frequent numbers. If the heap size is more than k,
        # we remove the smallest(top) number
        for num, frequency in num_frequency_map.items():
            heappush(top_k_elements, (frequency, num))
            if len(top_k_elements) > k:
                heappop(top_k_elements)

        # create a list of top k numbers
        top_numbers = []
        while top_k_elements:
            top_numbers.append(heappop(top_k_elements)[1])

        return top_numbers