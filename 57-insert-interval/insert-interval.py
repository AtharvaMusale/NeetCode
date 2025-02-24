class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
 
    
        result = []
        new_start, new_end = newInterval
        
        for index in range(len(intervals)):
            start, end = intervals[index]

            # If the current interval ends before the new interval starts, add it to the result
            if end < new_start:
                result.append([start, end])
            
            # If the current interval starts after the new interval ends, merge all remaining
            elif start > new_end:
                result.append([new_start, new_end])
                return result + intervals[index:]
            
            # Overlapping intervals, adjust the new_start and new_end
            else:
                new_start = min(start, new_start)
                new_end = max(end, new_end)
        
        # Add the final merged interval if it wasn't added in the loop
        result.append([new_start, new_end])
        return result