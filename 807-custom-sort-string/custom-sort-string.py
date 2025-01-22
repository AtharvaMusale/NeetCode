class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_count = Counter(s)
        string_builder = []
        for c in order:
            if c in s_count:
                string_builder.extend([c] * s_count[c])
            del s_count[c]
        

        for char, cnt in s_count.items():
            string_builder.extend([char] * cnt)
        
        return "".join(string_builder)