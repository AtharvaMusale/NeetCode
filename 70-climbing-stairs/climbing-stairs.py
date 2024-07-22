class Solution:
    def climbStairs(self, n: int) -> int:
        
        # dp = [0 for _ in range(n+1)]
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3,n+1):
        #     dp[n] = dp[n-1] + dp[n-2]
        # return dp[n] 

        def climb(n,memo):
            if n in memo:
                return memo[n]
            
            if n<=2:
                return n
            
            memo[n] = climb(n-1,memo) + climb(n-2,memo)
            return memo[n]
        
        return climb(n,{})



      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      






      
      
        # if n == 1:
        #     return 1
        
        # dp = [0 for _ in range((n+1))]
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3,n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        
        # return dp[n]


        

        

