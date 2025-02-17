class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if x == 1:
                return 1
            if n == 0:
                return 1
            r = n%2
            ans = power(x*x, n//2)
            if r:
                ans = ans * x
                return ans
            else:
                return ans
        
        res = power(x,abs(n))
        return res if n>=0 else 1/res