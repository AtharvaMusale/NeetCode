class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operation = ["+","-","*","/"]
        for c in tokens:
            if c in operation:
                if len(stack)>=2:
                    a = int(stack.pop())
                    b = int(stack.pop())
                    if c == "+":
                        stack.append(a+b)

                    elif c == "-":
                        stack.append(b-a)
                    elif c == "*":
                        stack.append(a*b)
                    elif c== "/":
                        stack.append(int(b/a))
            else:
                stack.append(int(c))
        return stack[0]