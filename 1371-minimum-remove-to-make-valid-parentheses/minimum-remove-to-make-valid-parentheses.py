class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # "lee(t(c)o)de)"
        # Add indices of ( in stack and anytime ) is encountered remove it
        # Whatever is remianing that can be ignore and join rest of the string
        stack = []
        indRemove = set()
        ans = ""
        for ind,val in enumerate(s):
            if val == "(":
                stack.append(ind)

            elif val == ")":
                if stack:
                    stack.pop()
                else:
                    indRemove.add(ind)            
        indRemove.update(stack)

        for ind, val in enumerate(s):
            if ind not in indRemove:
                # continue
                ans += val
        return ans
            
            
        