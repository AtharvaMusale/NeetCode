class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def clean(s):
            stack = []
            for i in s:
                if stack and i=="#":
                    stack.pop()
                elif i!="#":
                    stack.append(i)
            return stack
        
        return clean(s) == clean(t)

                
        # def remove_characters(s):
        #     stack = []
        #     for char in s:
        #         if char == '#' and stack:
        #             stack.pop()
        #         elif char != '#':
        #             stack.append(char)
        #     return stack

        # return remove_characters(s) == remove_characters(t)