class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []
        invalid_indices = set()
        for i,c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    invalid_indices.add(i)
            
        while stack:
            invalid_indices.add(stack.pop())
        
        res = []

        for i,c in enumerate(s):
            if not i in invalid_indices:
                res.append(c)
        return res
