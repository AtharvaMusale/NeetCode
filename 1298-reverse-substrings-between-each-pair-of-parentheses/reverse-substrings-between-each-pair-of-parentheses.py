class Solution:
    def reverseParentheses(self, s: str) -> str:
        open_parenthesis_indices = deque()
        res = []

        for i in range(len(s)):
            if s[i] == "(":
                open_parenthesis_indices.append(len(res))
            elif s[i] == ")":
                start = open_parenthesis_indices.pop()
                res[start:] = res[start:][::-1]
            else:
                res.append(s[i])
            
        return "".join(res)