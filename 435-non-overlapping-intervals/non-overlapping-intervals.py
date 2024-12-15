class Solution:
    def eraseOverlapIntervals(self, arr: List[List[int]]) -> int:
        # intervals.sort(key = lambda x:x[0])
        # prevEnd = intervals[0][1]
        # res = 0

        # for start, end in intervals[1:]:
        #     if start >= prevEnd:
        #         prevEnd = end
            
        #     else:
        #         res+=1
        #         prevEnd = min(end,prevEnd)
            
        # return res

        arr.sort(key = lambda x:x[0])
        prevEnd = arr[0][1]
        res = 0
        for start, end in arr[1:]:
            if start>=prevEnd:
                prevEnd = end
            else:
                res+=1
                prevEnd = min(prevEnd,end)
            
        return res