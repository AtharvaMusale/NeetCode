class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0

        result = 0
        sign = 1
        start = 0

        if s[0] == "-":
            sign = -1
            start = 1
        elif s[0] == "+":
            start = 1
        
        for char in s[start:]:
            if char.isdigit():
                result = 10 * result + int(char)
            else:
                break
        
        result *= sign
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN

        return result
