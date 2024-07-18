class Solution:
    def removeStars(self, s: str) -> str:
        cnt_stars = 0
        stack = []
        for i in s:
            stack.append(i)
            if i=="*":
                stack.pop()
                stack.pop()
        return "".join(stack)
            
