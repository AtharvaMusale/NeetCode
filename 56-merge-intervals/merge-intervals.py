class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        res = []
        current = intervals[0]
        
        for i in range(1, len(intervals)):
            if current[1] >= intervals[i][0]:  # There is an overlap
                current = [current[0], max(current[1], intervals[i][1])]
            else:
                res.append(current)
                current = intervals[i]
        
        res.append(current)  # Add the last interval
        
        return res