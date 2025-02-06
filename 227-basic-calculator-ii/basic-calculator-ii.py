class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        last_operator = "+"
        num = 0

        for i,c in enumerate(s):
            if c.isdigit():
                num = num*10 + int(c)
            
            if c in "+-*/" or i == len(s)-1:
                if last_operator == "+":
                    stack.append(num)
                elif last_operator == "-":
                    stack.append(-num)
                elif last_operator == "*":
                    stack.append(stack.pop() * num)
                elif last_operator == "/":
                    stack.append(int(stack.pop() / num))

                
                last_operator = c
                num = 0
        return sum(stack)