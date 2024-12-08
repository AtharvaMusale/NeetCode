class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")":"(", "]":"[","}":"{"}
        stack = []
        if s  == "":
            return True
        for char in s:
            if char in hashmap:
                top_element = stack.pop() if stack else "#"
                if hashmap[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

