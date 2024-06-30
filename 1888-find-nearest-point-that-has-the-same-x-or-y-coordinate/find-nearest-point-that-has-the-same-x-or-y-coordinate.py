class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        """ O(N)TS """
        valid = []
        for [a,b] in points:
            if a ==x or b ==y:
                valid.append([a,b])
        
        ans = min(valid , key = lambda t: abs(t[0]-x )+ abs(t[1]-y), default =None)
        if ans in points:
            return points.index(ans)
        
        else:
            return -1
