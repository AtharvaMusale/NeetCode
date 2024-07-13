class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = [0]

        operation = ["+","D","C"]

        for i in operations:

            if i == "+":
       
                ans = stack[-1] + stack[-2]
                stack.append(ans)
            elif i == "D":
                ans = stack[-1] * 2
                stack.append(ans)
            
            elif i == "C":
                stack.pop()
            else:
                stack.append(int(i))

        return sum(stack)