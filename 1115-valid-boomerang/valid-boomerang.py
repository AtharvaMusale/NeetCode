class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        if len(points)!=3:
            return -1
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]

        if (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1):
            return True
        else:
            return False