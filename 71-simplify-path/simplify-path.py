class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        for char in path:
            if char == "..":
                if stack:
                    stack.pop()
            elif char!= "." and char!="":
                stack.append(char)
        
        return "/" + "/".join(stack)