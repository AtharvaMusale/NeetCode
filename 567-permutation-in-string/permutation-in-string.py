class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def sort_string(s: str) -> str:
            return ''.join(sorted(s))
        
        sorted_s1 = sort_string(s1)
        len_s1 = len(s1)
        len_s2 = len(s2)
        
        for i in range(len_s2 - len_s1 + 1):
            if sort_string(s2[i:i + len_s1]) == sorted_s1:
                return True
        
        return False
