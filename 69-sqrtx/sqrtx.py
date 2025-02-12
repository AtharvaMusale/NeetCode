class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        l,r = 0, x // 2
        while l<=r:
            m = l + ((r-l)//2)
            d = m * m
            if d > x:
                r = m - 1
            elif d < x:
                l = m + 1
            else:
                return m
        return r