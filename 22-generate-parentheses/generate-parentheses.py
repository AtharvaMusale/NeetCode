class Solution:
    def __init__(self):
        self.result = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.solve(1,0,"(",n)
        return self.result

    def solve(self,open,close,curr,n):
        if open == n and open == close:
            self.result.append(curr)
            return 
        if open<n:
            self.solve(open+1, close, curr+"(",n)

        if close < open:
            self.solve(open, close+1, curr+")", n)







    # def __init__(self):
    #     self.result = []
    # def generateParenthesis(self, n: int) -> List[str]:
    #     self.solve(1, 0, "(", n)
    #     return self.result

    # def solve(self, open, close, curr, n):
    #     if open == n and open == close:
    #         self.result.append(curr)
    #         return

    #     if open < n:
            
    #         self.solve(open+1, close, curr+"(", n)
          
    #     if close < open:
          
    #         self.solve(open, close+1, curr+")", n)
            
        
        


        
        

# if stack empty : push ( curr (
# else:
#     Case 1: For each (, pop -> append )
#     Case 2: if frontRem > 0: push ( curRes (