class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        count = 0
        for i in s:
            if i == "(":
                stack.append(i)
            elif i == ")":
                stack.pop()
            else:
                continue
            count = max(count,len(stack))
        return count