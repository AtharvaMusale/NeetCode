class Solution:
    def reorganizeString(self, s: str) -> str:
        count = collections.Counter(s)
        heap = [(-c,char) for char,c in count.items()]
        heapq.heapify(heap)

        res = []
        while len(heap)>=2:
            top_count, top_char = heapq.heappop(heap)
            next_count, next_char = heapq.heappop(heap)
            res.append(top_char)
            res.append(next_char)
            if top_count+1:
                heapq.heappush(heap, (top_count+1, top_char))
            
            if next_count+1:
                heapq.heappush(heap, (next_count+1, next_char))

        if heap:
            top_count, top_char = heapq.heappop(heap)
            if top_count < -1 or (res and top_char == res[-1]):
                return ""
            else:
                res.append(top_char)
        return "".join(res)