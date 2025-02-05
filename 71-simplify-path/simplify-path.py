class Solution:
    def simplifyPath(self, path: str) -> str:
        #  single . -> current directory
        # .. -> previous directory
        # ////... -> /
        # ..... -> .
        stack = []
        path = path.split("/")
        # home, / , foo
        for c in path:
            if c == "..":
                if stack:
                    stack.pop()
            elif c and c != ".":
                stack.append(c)
        return "/" + "/".join(stack)