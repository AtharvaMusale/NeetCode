class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if n == 0:
                return 1
            
            if x == 0:
                return 0
            
            r = n % 2
            ans = helper(x*x, n//2)
            if r:
                return x * ans
            else:
                return ans
        
        res = helper(x, abs(n))
        return res if n>=0 else 1/res
