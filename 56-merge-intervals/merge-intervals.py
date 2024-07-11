class Solution:
    def merge(self, interval: List[List[int]]) -> List[List[int]]:
        interval.sort(key = lambda x:x[0])
        merged = [interval[0]]

        for i in range(1,len(interval)):

            start, end = interval[i]
            prev_start, prev_end = merged[-1]

            if prev_end>=start:
                merged[-1][1] = max(end,prev_end)
            else:
                merged.append(interval[i])

        return merged








# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         intervals.sort(key=lambda x: x[0])
#         merged = [intervals[0]]

#         for i in range(1, len(intervals)):
#             s2, e2 = intervals[i]
#             s1, e1 = merged[-1]

#             if s2 <= e1:
#                 merged[-1][1] = max(e1, e2)
#             else:
#                 merged.append(intervals[i])

#         return merged
            


