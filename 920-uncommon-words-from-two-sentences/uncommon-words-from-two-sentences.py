class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c1 = Counter(s1.split())
        c1 += Counter(s2.split())
        return [word for word in c1 if c1[word] ==1]