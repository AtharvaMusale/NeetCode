class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def backtrack(openC,closeC):
            if openC == closeC == n:
                res.append("".join(curr))
                return 
            
            if openC<n:
                curr.append("(")
                backtrack(openC+1, closeC)
                curr.pop()
            
            if closeC < openC:
                curr.append(")")
                backtrack(openC, closeC+1)
                curr.pop()

        backtrack(0,0)
        return res
            
