class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 2, x//2
        if x<2:
            return x

        while l<=r:
            pivot = l+((r-l)//2)
            nums = pivot * pivot
            if nums>x:
                r = pivot - 1
            elif nums<x:
                l = pivot + 1
            else:
                return pivot
        return r