import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+","-","*","/"]

        for t in tokens:
            if t in operations:
                if len(stack)>=2:
                    a = int(stack.pop())
                    b = int(stack.pop())
                    if t == "+":
                        stack.append(a+b)

                    elif t == "-":
                        stack.append(b-a)

                    elif t == "*":
                        stack.append(a*b)

                    elif t == "/":
                        stack.append(int(b/a))
            else:
                stack.append(int(t))
        return stack[0]
                    
