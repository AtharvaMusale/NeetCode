class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        base = intervals[0][1]
        res = 0
        for i in range(1,len(intervals)):
            curr = intervals[i]

            if curr[0]<base:
                res+=1
                base = min(base,curr[1])
            
            else:
                base = curr[1]

        return res

        # intervals.sort()

        # currMinEnd = intervals[0][1]
        # res = 0

        # for i in range(1,len(intervals)):
        #     currInterval = intervals[i]

        #     if currInterval[0] < currMinEnd:        
        #         res += 1
        #         currMinEnd = min(currMinEnd, currInterval[1])
        #     else:
        #         currMinEnd = currInterval[1]

        # return res
