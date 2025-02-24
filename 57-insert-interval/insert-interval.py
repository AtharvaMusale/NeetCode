from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # First, we need to insert the newInterval into intervals, then sort the entire list
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        # Initialize the result list with the first interval
        res = [intervals[0]]

        # Iterate through the sorted intervals starting from the second interval
        for i in range(1, len(intervals)):
            currStart, currEnd = intervals[i]
            lastEnd = res[-1][1]

            # Check if the current interval overlaps with the last interval in res
            if currStart <= lastEnd:
                # If they overlap, merge the current interval into the last interval of res
                res[-1][1] = max(lastEnd, currEnd)
            else:
                # If they do not overlap, add the current interval to res
                res.append([currStart, currEnd])

        return res
