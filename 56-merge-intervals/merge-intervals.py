class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Sort the intervals based on the start time.
        intervals.sort(key=lambda x: x[0])
        res = []

        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                # If there's no overlap, add the current interval to the result.
                res.append(interval)
            else:
                # There is an overlap, so merge by extending the end of the last interval in the result.
                res[-1][1] = max(res[-1][1], interval[1])

        return res
