class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l_count = r_count = 0
        added = 0
        for c in s:
            if c == "(":
                l_count+=1
            else:
                if l_count>r_count:
                    r_count+=1
                else:
                    added+=1
        added += (l_count-r_count)
        return added

