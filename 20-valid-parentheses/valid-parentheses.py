class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")":"(", "}":"{","]":"["}
        stack = []

        for i in s:
            if i not in hashmap:
                stack.append(i)
                continue
            
            if not stack or stack[-1] != hashmap[i]:
                return False
            
            stack.pop()
            
        return not stack

class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack
